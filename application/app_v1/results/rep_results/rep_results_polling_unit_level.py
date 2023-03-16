from app.application.app_v1.database import get_db,get_db2
from app.application.app_v1.results.rep_results.partytable import presidential_table_pu

import json





#  ward results

def get__polling_ward_all_results(country_name="undefined",state_name="undefined", constituency_name="undefined",lga_name="undefined", ward_name="undefined"):
    with get_db() as conn:
        cur = conn.cursor()


        constituency_query = ""  
        country_query = ""
        state_query = ""
        lga_query = ""
        ward_query = ""

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if constituency_name and constituency_name != "undefined":
            constituency_query = f" AND house_id={constituency_name}"
        if lga_name and lga_name != "undefined":
            lga_query = f" AND lga_id={lga_name}"
        if ward_name and ward_name != "undefined":
            ward_query = f" AND ward_id={ward_name}"
      
      

        ward_result = f"""{presidential_table_pu['query']}  select ward_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted from wt where 1=1 {state_query} {constituency_query} {lga_query} {ward_query} """
        pu_result = f"""{presidential_table_pu['query']} select pu_code,pu_name, NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP,
 Total_Registered_voters,  Total_Accredited_voters, Total_Rejected_votes, remarks from pu   where 1=1 {state_query} {constituency_query} {lga_query} {ward_query} order by pu_id"""

        key_values = []
        execute_queries = []
        execute_queries.append(ward_result)
        key_values.append("result")
        execute_queries.append(pu_result)
        key_values.append("puresult")

        query =[]
        ress = {}
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    ress[key_values[index]] = results
                except:
                    print('Skipped a sceanrio')
        
        return ress

     


# lga results

def get_polling_lga_all_results(country_name="undefined",state_name="undefined", constituency_name="undefined",lga_name="undefined"):
    with get_db() as conn:
        cur = conn.cursor()
    
        constituency_query = ""
        country_query = ""
        state_query = ""
        lga_query = ""
   
     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if constituency_name and constituency_name != "undefined":
            constituency_query = f" AND house_id={constituency_name}"
        if lga_name and lga_name != "undefined":
            lga_query = f" AND lga_id={lga_name}"
   
     
        lga_result = f"""{presidential_table_pu['query']} select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted  from lgat  where 1=1 {state_query} {constituency_query} {lga_query} """
        pu_result = f"""{presidential_table_pu['query']}  select ward_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted from wt  where 1=1 {state_query} {constituency_query} {lga_query} order by ward_id """

        key_values = []
        execute_queries = []
       
        execute_queries.append(lga_result)
        key_values.append("result")
        execute_queries.append(pu_result)
        key_values.append("puresult")

        query =[]
        ress={}
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    ress[key_values[index]] = results
                except:
                    print('Skipped a sceanrio')
        
        return ress
        

# state results

def get_polling_state_all_results(country_name="undefined",state_name="undefined",constituency_name="undefined"):
    with get_db() as conn:
        cur = conn.cursor()

        constituency_query = ""
        country_query = ""
        state_query = ""
      

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if constituency_name and constituency_name != "undefined":
            constituency_query = f" AND house_id={constituency_name}"
       
     

        state_result = f"""{presidential_table_pu['query']}  select house_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted  from house where 1=1 {state_query} {constituency_query}"""
        pu_result = f"""{presidential_table_pu['query']} select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
  		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted from lgat where 1=1 {state_query} {constituency_query} order by lga_id """
        key_values = []
        execute_queries = []
    
        execute_queries.append(state_result)
        key_values.append("result")
        execute_queries.append(pu_result)
        key_values.append("puresult")


        query =[]
        ress = {}
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    ress[key_values[index]] = results
                except:
                    print('Skipped a sceanrio')
        
        return ress
 