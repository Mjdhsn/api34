from app.application.app_v1.database import get_db,get_db2
from app.application.app_v1.results.rep_results.partytable import presidential_table_state
import json






# state results

def get_state_state_all_results(country_name="undefined",state_name="undefined",constituency_name="undefined"):
       with get_db() as conn:
        cur = conn.cursor()

         
        country_query = ""
        state_query = ""
        constituency_query =""

      

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if constituency_name and constituency_name != "undefined":
            constituency_query = f" AND house_id={constituency_name}"
       
    

        state_result = f"""{presidential_table_state['query']}   select house_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
     	  Total_Registered_voters,  total_valid_votes_c AS total_valid_votes, Total_Rejected_votes, total_votes_cast_c AS total_vote_casted FROM house where 1=1 {state_query} ORDER BY house_id """

        key_values = []
        execute_queries = []
        
        execute_queries.append(state_result)
        key_values.append("result")

        result = ['result']
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
       