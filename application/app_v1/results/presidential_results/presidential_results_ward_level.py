from app.application.app_v1.database import get_db,get_db2
from app.application.app_v1.results.presidential_results.partytable import presidential_table_ward
import json




# lga results

def get_ward_lga_all_results(country_name="undefined",state_name="undefined", lga_name="undefined",party_data={}):
    with get_db() as conn:
        cur = conn.cursor()
    
        country_query = ""
        state_query = ""
        lga_query = ""
   
     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if lga_name and lga_name != "undefined":
            lga_query = f" AND lga_id={lga_name}"
   
     

        lga_result = f"""{presidential_table_ward['query']} select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,Total_Accredited_voters,total_valid_votes,Total_Rejected_votes,total_vote_casted,remarks from lgat where 1=1 {state_query} {lga_query} """
        ward_result= f"""{presidential_table_ward['query']}  select ward_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,Total_Accredited_voters,total_valid_votes,Total_Rejected_votes,total_vote_casted,remarks from wt  where 1=1  {state_query} {lga_query}  order by ward_id """
        key_values = []
 
        execute_queries = []
        execute_queries.append(lga_result)
        key_values.append("result")
        execute_queries.append(ward_result)
        key_values.append("puresult")

        ress = {}

        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    ress[key_values[index]] = results
                except:
                    print('Skipped a sceanrio')
        
        return ress

        


# state results

def get_ward_state_all_results(country_name="undefined",state_name="undefined",party_data={}):
      with get_db() as conn:
        cur = conn.cursor()

         
        country_query = ""
        state_query = ""
      

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
       
    

        state_result = f"""{presidential_table_ward['query']} select state_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,Total_Accredited_voters,total_valid_votes,Total_Rejected_votes,total_vote_casted,remarks from st where 1=1 {state_query} """
        lga_result = f"""{presidential_table_ward['query']}  select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,Total_Accredited_voters,total_valid_votes,Total_Rejected_votes,total_vote_casted,remarks from lgat    where 1=1 {state_query}  order by lga_id"""
        key_values = []
        execute_queries = []
    
        execute_queries.append(state_result)
        key_values.append("result")
        execute_queries.append(lga_result)
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

        


#  country result table


def get_ward_country_all_results(country_name,party_data={}):
     with get_db() as conn:
        cur = conn.cursor()
           
        country_query = ""     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
      
    

        country_result = f"""{presidential_table_ward['query']}  where 1=1 """
        state_result = f"""{presidential_table_ward['query']}  order by state_id """
        key_values = []
        execute_queries = []
    
        execute_queries.append(country_result)
        key_values.append("result")
        execute_queries.append(state_result)
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

      
        

    