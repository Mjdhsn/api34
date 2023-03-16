from application.app_v1.database import get_db2,get_db
from datetime import datetime

# Get PollingUnit


def getPollingUnitbadge(state, lga, wardID):
    with get_db() as conn:
        cur = conn.cursor()

        
        # wardID = int(wardID) % 12
        sql = f"""SELECT pu_id, pu_name, pu_code FROM pu_result_table WHERE 
        state_id = {state} AND 
        lga_id = {lga} AND
        ward_id =  {wardID}"""
        try:
            cur.execute(sql)
            results = cur.fetchall()
            
            
            json_data1 = []
            json_data2 = []
            json_data3 = []
            for row in results:
                sql = f"""SELECT COUNT(*) as  count1 FROM userdata_pu WHERE file_type=0 AND state_id = {state} AND lga_id = {lga} AND  ward_id = {wardID} AND pu_id ={row['pu_id']}"""
                cur.execute(sql)
                row['images'] = cur.fetchone()
                sql = f"""SELECT COUNT(*) as  count1 FROM userdata_pu WHERE file_type=1 AND state_id = {state} AND lga_id = {lga} AND  ward_id = {wardID} AND pu_id =  {row['pu_id']}"""
                cur.execute(sql)
                row['videos'] = cur.fetchone()
                json_data1.append(row['pu_id'])
                json_data2.append(row['pu_name'])
                json_data3.append(row['pu_code'])
            return [json_data1]+[json_data2]+[json_data3]+[results]
        except Exception as e:
            print(e)
            return str(e)

import json
def getPollingUnit(state_name, lga_name, wardID):
    with get_db() as conn:
        cur = conn.cursor()

        
        # wardID = int(wardID) % 12
     
        sql = f"""SELECT pu_id, pu_name, pu_code FROM pu_result_table WHERE 
        state_id = {state_name} AND 
        lga_id = {lga_name} AND
        ward_id =  {wardID}"""
        try:
            cur.execute(sql)
            results = cur.fetchall()
            
            json_data1 = []
            json_data2 = []
            json_data3 = []
            for row in results:
                json_data1.append(row['pu_id'])
                json_data2.append(row['pu_name'])
                json_data3.append(row['pu_code'])
            return [json_data1]+[json_data2]+[json_data3] + [results]
        except Exception as e:
            print(e)
            return str(e)


def getPollingUnitsenate(state_name, senate_district,lga_name, ward_name):
    with get_db() as conn:
        cur = conn.cursor()

        sql = f"select state_id, state_name, district_id, district_name,lga_id, lga_name, ward_id ,ward_name,pu_id, pu_name,pu_code from sen_pu_table where state_id={state_name} and district_id ={senate_district} and lga_id={lga_name}  and ward_id={ward_name}"
    
        try:
            cur.execute(sql)
            results = cur.fetchall()
            
            
            json_data1 = []
            json_data2 = []
            json_data3 = []
            res = {}
  
            for row in results:
                json_data1.append(row['pu_id'])
                json_data2.append(row['pu_name'])
                json_data3.append(row['pu_code'])
     
            return [json_data1] + [json_data2] + [json_data3] + [results]
        except Exception as e:
            print(e)
            return str(e)


def getPollingUnitrep(state_name, constituency_name,lga_name, ward_name):
    with get_db() as conn:
        cur = conn.cursor()

        sql = f"select  state_id, state_name,house_id,house_name, lga_id, lga_name,ward_id ,ward_name,pu_id,pu_name,pu_code from house_pu_table where state_id={state_name} and house_id ={constituency_name} and lga_id={lga_name}  and ward_id={ward_name}"
    
        try:
            cur.execute(sql)
            results = cur.fetchall()
          
            json_data1 = []
            json_data2 = []
            json_data3 = []
            res = {} 
            for row in results:
                json_data1.append(row['pu_id'])
                json_data2.append(row['pu_name'])
                json_data3.append(row['pu_code'])
     
            return [json_data1] + [json_data2] + [json_data3] + [results]
        except Exception as e:
            print(e)
            return str(e)






# Get PollingUnit
def getPUResult(country_name,state_name,lga_name,ward_name,pu_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM pu_result_table where  state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql1 = f"SELECT * FROM userdata_pu WHERE  state_id = {state_name} AND lga_id= {lga_name} AND ward_id = {ward_name} AND pu_id = {pu_name}"

        final ={}
        try:
            cur.execute(sql)

            results = cur.fetchall()
            
            cur.execute(sql1)
            results1 = cur.fetchall()
            parties = ["A","AA","AAC","ADC","ADP","APC","APGA","APM","APP","BP","LP","NNPP","NRM","PDP","PRP","SDP","YPP","ZLP"]
            total =["Total_Accredited_voters","Total_Registered_voters","Total_Rejected_votes","total_valid_votes_c"]    
    
            data = ['date_time', 'person_collated','file']
            parties_results = {}
            total_results={}
            other_data_results={}
            for key in parties:
                parties_results.update( {key:results[0][key]})
               
            for key in total:
                total_results.update( {key:results[0][key]})

            for key in data:
                other_data_results.update( {key:results[0][key]})

            final['results'] = parties_results
            final['total'] = total_results
            final['other_data'] = other_data_results
            final['media'] = results1

            return final
        except Exception as e:
            print(e)
            return str(e)

def getPUResultsenate(country_name,state_name,senate_district,lga_name,ward_name,pu_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM sen_pu_table where  state_id = {state_name} and district_id={senate_district} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql1 = f"SELECT * FROM userdata_pu WHERE  state_id = {state_name} AND lga_id= {lga_name} AND ward_id = {ward_name} AND pu_id = {pu_name}"

        final ={}
        try:
            cur.execute(sql)

            results = cur.fetchall()
            
            
            cur.execute(sql1)
            results1 = cur.fetchall()
            parties = ["A","AA","AAC","ADC","ADP","APC","APGA","APM","APP","BP","LP","NNPP","NRM","PDP","PRP","SDP","YPP","ZLP"]
            total =["Total_Accredited_voters","Total_Registered_voters","Total_Rejected_votes","total_valid_votes_c"]    
    
            data = ['date_time', 'person_collated','file']
            parties_results = {}
            total_results={}
            other_data_results={}
            for key in parties:
                parties_results.update( {key:results[0][key]})
               
            for key in total:
                total_results.update( {key:results[0][key]})

            for key in data:
                other_data_results.update( {key:results[0][key]})

            final['results'] = parties_results
            final['total'] = total_results
            final['other_data'] = other_data_results
            final['media'] = results1

            return final
        except Exception as e:
            print(e)
            return str(e)

def getPUResultrep(country_name,state_name,constituency_name,lga_name,ward_name,pu_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM house_pu_table where  state_id = {state_name} and house_id={constituency_name}  and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql1 = f"SELECT * FROM userdata_pu WHERE  state_id = {state_name} AND lga_id= {lga_name} AND ward_id = {ward_name} AND pu_id = {pu_name}"

        final ={}
        try:
            cur.execute(sql)

            results = cur.fetchall()
            
            
            cur.execute(sql1)
            results1 = cur.fetchall()
            parties = ["A","AA","AAC","ADC","ADP","APC","APGA","APM","APP","BP","LP","NNPP","NRM","PDP","PRP","SDP","YPP","ZLP"]
            total =["Total_Accredited_voters","Total_Registered_voters","Total_Rejected_votes","total_valid_votes_c"]    
    
            data = ['date_time', 'person_collated','file']
            parties_results = {}
            total_results={}
            other_data_results={}
            for key in parties:
                parties_results.update( {key:results[0][key]})
               
            for key in total:
                total_results.update( {key:results[0][key]})

            for key in data:
                other_data_results.update( {key:results[0][key]})

            final['results'] = parties_results
            final['total'] = total_results
            final['other_data'] = other_data_results
            final['media'] = results1

            return final
        except Exception as e:
            print(e)
            return str(e)
            



def updatePUResult(country_name,state_name,lga_name,ward_name,pu_name, data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update pu_result_table SET {query} , date_time ='{timer}',status='collated' where  state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql2 = f"""Select * from pu_result_table Where   state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        
        try:
            cur.execute(sql)
            # results = cur.fetchall()
            
            conn.commit()
            cur.execute(sql2)
            results = cur.fetchall()
            
            
            res= {}
            for row in results:
                res.update({'person_collated':row['person_collated']})
                res.update({"time":row['date_time']})
            return res
        except Exception as e:
            print(e)
            return str(e)

def updatePUResultsenate(country_name,state_name,senate_district,lga_name,ward_name,pu_name, data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update sen_pu_table SET {query} , date_time ='{timer}',status='collated' where  state_id = {state_name} and district_id ={senate_district} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql2 = f"""Select * from sen_pu_table Where  state_id = {state_name} and district_id ={senate_district} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        try:
            cur.execute(sql)
            # results = cur.fetchall()
            conn.commit()
            cur.execute(sql2)
            results = cur.fetchall()
            
            
            res= {}
            for row in results:
                res.update({'person_collated':row['person_collated']})
                res.update({"time":row['date_time']})
            return res
        except Exception as e:
            print(e)
            return str(e)

def updatePUResultrep(country_name,state_name,constituency_name,lga_name,ward_name,pu_name, data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update house_pu_table SET {query} , date_time ='{timer}',status='collated' where  state_id = {state_name} and house_id ={constituency_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql2 = f"""Select * from house_pu_table Where  state_id = {state_name} and house_id ={constituency_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        try:
            cur.execute(sql)
            # results = cur.fetchall()
            conn.commit()
            cur.execute(sql2)
            results = cur.fetchall()
            
            
            res= {}
            for row in results:
                res.update({'person_collated':row['person_collated']})
                res.update({"time":row['date_time']})
            return res
        except Exception as e:
            print(e)
            return str(e)


def cancelPUResult(country_name,state_name,lga_name,ward_name,pu_name, data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update pu_result_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0,YPP=0, ZLP=0 , date_time ='{timer}' where  state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql2 = f"""Select * FROM pu_result_table  Where  state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        try:
            cur.execute(sql)
            conn.commit()
            cur.execute(sql2)
            results = cur.fetchall()
            
            
            res= {}
            for row in results:
                res.update({'person_collated':row['person_collated']})
                res.update({"time":row['date_time']})
            return res
        except Exception as e:
            print(e)
            return str(e)



def cancelPUResultsenate(country_name,state_name,senate_district,lga_name,ward_name,pu_name, data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update sen_pu_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}' where state_id = {state_name} and district_id ={senate_district} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql2 = f"""Select * FROM sen_pu_table  Where  state_id = {state_name} and district_id ={senate_district} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        try:
            cur.execute(sql)
            conn.commit()
            cur.execute(sql2)
            results = cur.fetchall()
            
            
            res= {}
            for row in results:
                res.update({'person_collated':row['person_collated']})
                res.update({"time":row['date_time']})
            return res
        except Exception as e:
            print(e)
            return str(e)



def cancelPUResultsrep(country_name,state_name,constituency_name,lga_name,ward_name,pu_name, data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update house_pu_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}' where  state_id = {state_name} and house_id ={constituency_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        sql2 = f"""Select * FROM house_pu_table  Where  state_id = {state_name} and house_id ={constituency_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        try:
            cur.execute(sql)
            conn.commit()
            cur.execute(sql2)
            results = cur.fetchall()
            
            
            res= {}
            for row in results:
                res.update({'person_collated':row['person_collated']})
                res.update({"time":row['date_time']})
            return res
        except Exception as e:
            print(e)
            return str(e)