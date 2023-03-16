from application.app_v1.database import get_db,get_db2
from application.app_v1.results.rep_results.partytable import presidential_table_lga
import json



       

# state results

def get_lga_state_all_results(country_name="undefined",state_name="undefined",constituency_name="undefined",party_data={}):
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
       
     

        state_result = f"""{presidential_table_lga['query']}  select house_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,  total_valid_votes, Total_Rejected_votes, total_vote_casted  from house where 1=1 {state_query} {constituency_query}"""
        pu_result = f"""{presidential_table_lga['query']} select lga_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
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

        

    