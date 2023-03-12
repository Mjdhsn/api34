import pandas as pd
import boto3
import cv2
import snowflake.connector

s3 = boto3.resource('s3')
bucket = "electionuploads104030-dev" 
df =  pd.read_csv('presidentialPdf3.csv')
from pdf2image import convert_from_path
import urllib.request
import shutil
import re
import difflib


import io
import math
import sys
import numpy as np
from PIL import Image
import json
import uuid


def extract_text(response, extract_by="WORD"):
    line_text = []
    for block in response["Blocks"]:
        if block["BlockType"] == extract_by:
            line_text.append(block["Text"])
    return line_text


def map_word_id(response):
    word_map = {}
    for block in response["Blocks"]:
        if block["BlockType"] == "WORD":
            word_map[block["Id"]] = block["Text"]
        if block["BlockType"] == "SELECTION_ELEMENT":
            word_map[block["Id"]] = block["SelectionStatus"]
    return word_map


def extract_table_info(response, word_map):
    row = []
    table = {}
    ri = 0
    flag = False

    for block in response["Blocks"]:
        if block["BlockType"] == "TABLE":
            key = f"table_{uuid.uuid4().hex}"
            table_n = +1
            temp_table = []

        if block["BlockType"] == "CELL":
            if block["RowIndex"] != ri:
                flag = True
                row = []
                ri = block["RowIndex"]

            if "Relationships" in block:
                for relation in block["Relationships"]:
                    if relation["Type"] == "CHILD":
                        row.append(" ".join([word_map[i] for i in relation["Ids"]]))
            else:
                row.append(" ")

            if flag:
                temp_table.append(row)
                table[key] = temp_table
                flag = False
    return table


def get_key_map(response, word_map):
    key_map = {}
    for block in response["Blocks"]:
        if block["BlockType"] == "KEY_VALUE_SET" and "KEY" in block["EntityTypes"]:
            for relation in block["Relationships"]:
                if relation["Type"] == "VALUE":
                    value_id = relation["Ids"]
                if relation["Type"] == "CHILD":
                    v = " ".join([word_map[i] for i in relation["Ids"]])
                    key_map[v] = value_id
    return key_map


def get_value_map(response, word_map):
    value_map = {}
    for block in response["Blocks"]:
        if block["BlockType"] == "KEY_VALUE_SET" and "VALUE" in block["EntityTypes"]:
            if "Relationships" in block:
                for relation in block["Relationships"]:
                    if relation["Type"] == "CHILD":
                        v = " ".join([word_map[i] for i in relation["Ids"]])
                        value_map[block["Id"]] = v
            else:
                value_map[block["Id"]] = "VALUE_NOT_FOUND"

    return value_map


def get_kv_map(key_map, value_map):
    final_map = {}
    for i, j in key_map.items():
        final_map[i] = "".join(["".join(value_map[k]) for k in j])
    return final_map
def JPEGSaveWithTargetSize(im, filename, target):
   """Save the image as JPEG with the given name at best quality that makes less than "target" bytes"""
   # Min and Max quality
   Qmin, Qmax = 25, 96
   # Highest acceptable quality found
   Qacc = -1
   while Qmin <= Qmax:
      m = math.floor((Qmin + Qmax) / 2)

      # Encode into memory and get size
      buffer = io.BytesIO()
      im.save(buffer, format="JPEG", quality=m)
      s = buffer.getbuffer().nbytes

      if s <= target:
         Qacc = m
         Qmin = m + 1
            
      elif s > target:
         Qmax = m - 1

   # Write to disk at the defined quality
   if Qacc > -1:
      im.save(filename, format="JPEG", quality=Qacc)
   else:
      print("ERROR: No acceptble quality factor found", file=sys.stderr)
import pandas as pd
import boto3
import cv2
import snowflake.connector

s3 = boto3.resource('s3')
bucket = "electionuploads104030-dev" 
df =  pd.read_csv('presidentialPdf16k.csv')
from pdf2image import convert_from_path
import urllib.request
import shutil
import re
import difflib
def get_db2():
    return snowflake.connector.connect(

    user= 'maryam',
    password = 'Maryam01?',
    account = 'yloufpv-js63877',
    database='LOGEECAI',
    schema = 'PUBLIC',
    warehouse='LOGEEC',
)



for index, row in df.iterrows():
    pu_code = row['Pu Code']
    image_url = row['Result Pdf']
    urllib.request.urlretrieve(image_url, "filename.pdf")
    pil_image_lst = convert_from_path('filename.pdf')
    pil_image = pil_image_lst[0]
    pil_image.save("images/"+"real/"+"result"+str(index)+".jpg")
    pu_name = pu_code.replace('/','-')
    JPEGSaveWithTargetSize(pil_image, f"images/{pu_name}.jpg", 4000000)
    img = cv2.imread(f"images/{pu_name}.jpg")
    image_string = cv2.imencode('.png', img)[1].tobytes()
    image_name = f"collation/photos/{pu_name}.jpg"
    
    s3.Bucket(bucket).put_object(Key=image_name, Body=image_string, 
                                ContentType="image/png", ACL="public-read")
    
    try:
        textract = boto3.client("textract")
        response = textract.analyze_document(Document={'Bytes': image_string}, FeatureTypes=["FORMS", "TABLES"])
        raw_text = extract_text(response, extract_by="LINE")
        word_map = map_word_id(response)
        table = extract_table_info(response, word_map)
        key_map = get_key_map(response, word_map)
        value_map = get_value_map(response, word_map)
        final_map = get_kv_map(key_map, value_map)
        for key,value in table.items():
            table = value
        total_register = ""
        total_acrredited =""
        total_rejected = ""
        spoilled =""
        valid_votes =""
        used_ballot =""
        ballot_issued = ""
        unused_ballot = ""
        for key,value in final_map.items():
            if "Voters on the Register" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                total_register += f"TOTAL_REGISTERED_VOTERS ={value}"

            elif "Accredited" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                total_acrredited += f"TOTAL_ACCREDITED_VOTERS ={int(value)}"
            elif "Rejected" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                total_rejected += f"TOTAL_REJECTED_VOTES={value}"
            elif "Spoilled" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                spoilled += f"SPOILED_BALLOT={value}"
            elif "Total Valid Votes" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                valid_votes += f"VALID_VOTES_C ={value}"
            elif "Used Ballots Papers" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                used_ballot += f"USED_BALLOT ={value}"
            elif "Ballot Papers Issued" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                ballot_issued += f"BALLOT_ISSUED ={value}"
            elif "Unused Ballot Papers" in key:
                value= re.sub("\D","",value)
                if value =="":
                    value = 0
                value = int(value)
                unused_ballot += f"UNUSED_BALLOT ={value}"
            else:
                pass

        numberlist= [total_register,total_acrredited,total_rejected,spoilled,valid_votes,used_ballot,ballot_issued,unused_ballot]    
        numberlist = [x for x in numberlist if x != ""]
        numberquery = ", ".join(numberlist)








        party_real_values = ['A', 'AA', 'AAC', 'ADC', 'ADP', 'APC', 'APGA', 'APM', 'APP', 'BP', 'LP', 'NNPP', 'NRM', 'PDP', 'PRP', 'SDP','YPP', 'ZLP']
        table_values = table[2:]
        final_list = []
        party_val = []
        party_values = []
        for i, val in enumerate(table_values):
            values  =  val[2:3][0]
            party = val[1:2][0]
            party_val.append(party)
            party_values.append(values)

        party_val = [x for x in party_val if x != ' ']
        # valuess = [x for x in valuess if x != ' ']
        party_matching = []
        for p in party_val:

            v = difflib.get_close_matches(p, party_real_values)
            if p =="POP":
                v[0] = "PDP"
            elif p =="AOP":
                v[0] = "ADP"
            elif p =="SOP":
                v[0] ="SDP"
            elif p =="AOC":
                v[0] ="ADC"
            party_matching.append(v[0])
        values_matching = []


        for v in party_values:
            n= re.sub("\D","",v)
            if n =="":
                n = 0
            n = int(n)
            values_matching.append(n)

        party_dictionary =  dict(zip(party_matching,values_matching))





   



        part = ""
        for key, value in party_dictionary.items():
            part += f"{key} ={value},"
        part = part[:-1]
  

         
        table_name = "PU_RESULT_TABLE"
        final_query = f"Update {table_name} SET {part},{numberquery},status='collated' where pu_code={pu_code}"
        sql = f"""Update PU_RESULT_TABLE SET file='{image_name}' Where pu_code={pu_code}"""

        with get_db2() as conn:
            cur = conn.cursor()
            try:
                cur.execute(final_query)
                cur.execute(sql)
                print('Done', pu_code)
            except:
                print('error in sql')
    except:
        print('failed')

  






















