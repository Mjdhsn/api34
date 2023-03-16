from application.app_v1.database import get_db,get_db2
from application.app_v1.results.senate_results.partytable import presidential_table_pu

import json



   

     


#  ward results

def get__polling_ward_all_results(country_name="undefined",state_name="undefined", district_name="undefined",lga_name="undefined", ward_name="undefined"):
    with get_db2() as conn:
        cur = conn.cursor()


        district_query = ""  
        country_query = ""
        state_query = ""
        lga_query = ""
        ward_query = ""

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if district_name and district_name != "undefined":
            district_query = f" AND district_id={district_name}"
        if lga_name and lga_name != "undefined":
            lga_query = f" AND lga_id={lga_name}"
        if ward_name and ward_name != "undefined":
            ward_query = f" AND ward_id={ward_name}"
  

        ward_result = f"""{presidential_table_pu['query']}  select ward_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted from wt where 1=1 {state_query} {district_query} {lga_query} {ward_query} """
        pu_result = f"""{presidential_table_pu['query']}  select pu_code,pu_name, NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP,
 Total_Registered_voters,  Total_Accredited_voters, Total_Rejected_votes, remarks from pu where 1=1 {state_query} {district_query} {lga_query} {ward_query} order by pu_id """

        key_values = []
        execute_queries = []
      
        execute_queries.append(ward_result)
        key_values.append("result")
        execute_queries.append(pu_result)
        key_values.append("puresult")

        query =[]
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute_async(sql)
                    query.append(cur.sfqid)
                except:
                    print('Skipped a sceanrio')
        ress = {}
        ress2 ={}
        import time
        while True:

            for result in query:
                status = conn.get_query_status(result)
                if str(status) == 'QueryStatus.SUCCESS':
                    
                    index = query.index(result)
                    key = key_values[index]
                    cur.get_results_from_sfqid(result)
                    val_results = cur.fetch_pandas_all()
                    val_results = val_results.to_json(orient="records")
                    val_results = json.loads(val_results)
                    # res = ret.to_json(orient="records")
                    # parsed = json.loads(res)
                    ress[key] = val_results                      
                else :
                    time.sleep(0.03)
            if len(ress) ==len(execute_queries):
                break
        ress2['result'] = ress['result']
        ress2['puresult'] = ress['puresult']
        return ress2
        

     


# lga results

def get_polling_lga_all_results(country_name="undefined",state_name="undefined", district_name="undefined",lga_name="undefined"):
    with get_db2() as conn:
        cur = conn.cursor()
    
        district_query = ""
        country_query = ""
        state_query = ""
        lga_query = ""
   
     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if district_name and district_name != "undefined":
            district_query = f" AND district_id={district_name}"
        if lga_name and lga_name != "undefined":
            lga_query = f" AND lga_id={lga_name}"
   
   

        lga_result = f"""{presidential_table_pu['query']}  select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted  from lgat where 1=1 {state_query} {district_query} {lga_query} """
        pu_result = f"""{presidential_table_pu['query']}    select ward_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted from wt where 1=1 {state_query} {district_query} {lga_query} order by ward_id """

        key_values = []
        execute_queries = []
        
        execute_queries.append(lga_result)
        key_values.append("result")
        execute_queries.append(pu_result)
        key_values.append("puresult")


        query =[]
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute_async(sql)
                    query.append(cur.sfqid)
                except:
                    print('Skipped a sceanrio')
        ress = {}
        ress2={}
        import time
        while True:

            for result in query:
                status = conn.get_query_status(result)
                if str(status) == 'QueryStatus.SUCCESS':
                    
                    index = query.index(result)
                    key = key_values[index]
                    cur.get_results_from_sfqid(result)
                    val_results = cur.fetch_pandas_all()
                    val_results = val_results.to_json(orient="records")
                    val_results = json.loads(val_results)
                    # res = ret.to_json(orient="records")
                    # parsed = json.loads(res)
                    ress[key] = val_results                      
                else :
                    time.sleep(0.03)
            if len(ress) ==len(execute_queries):
                break
        ress2['result'] = ress['result']
        ress2['puresult'] = ress['puresult']
        return ress2

        

# state results

def get_polling_state_all_results(country_name="undefined",state_name="undefined",district_name="undefined"):
    with get_db2() as conn:
        cur = conn.cursor()

        district_query = ""
        country_query = ""
        state_query = ""
      

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if district_name and district_name != "undefined":
            district_query = f" AND district_id={district_name}"
       
    

        state_result = f"""{presidential_table_pu['query']}    select district_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted  from dist where 1=1 {state_query} {district_query}"""
        pu_result = f"""{presidential_table_pu['query']}  select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted from lgat where  1=1 {state_query} {district_query} order by lga_id  """
        key_values = []
        execute_queries = []
        execute_queries.append(pu_result)
        key_values.append("puresult")

        execute_queries.append(state_result)
        key_values.append("result")


        query =[]
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute_async(sql)
                    query.append(cur.sfqid)
                except:
                    print('Skipped a sceanrio')
        ress = {}
        ress2={}
        import time
        while True:

            for result in query:
                status = conn.get_query_status(result)
                if str(status) == 'QueryStatus.SUCCESS':
                    
                    index = query.index(result)
                    key = key_values[index]
                    cur.get_results_from_sfqid(result)
                    val_results = cur.fetch_pandas_all()
                    val_results = val_results.to_json(orient="records")
                    val_results = json.loads(val_results)
                    # res = ret.to_json(orient="records")
                    # parsed = json.loads(res)
                    ress[key] = val_results                      
                else :
                    time.sleep(0.03)
            if len(ress) ==len(execute_queries):
                break
        ress2['result'] = ress['result']
        ress2['puresult'] = ress['puresult']
        return ress2

 