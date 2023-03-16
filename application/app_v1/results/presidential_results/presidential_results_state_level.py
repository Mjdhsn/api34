from app.application.app_v1.database import get_db,get_db2
from app.application.app_v1.results.presidential_results.partytable import presidential_table_state
import json



#  country result table


def get_state_country_all_results(country_name,party_data={}):
      with get_db() as conn:
        cur = conn.cursor()
           
        country_query = ""     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
      
    

  
        state_result = f"""{presidential_table_state['query']} select state_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
		 Total_Registered_voters, Total_Accredited_voters, total_valid_votes AS total_valid_votes, Total_Rejected_votes, total_vote_casted AS total_vote_casted,remarks from st order by state_id """
        key_values = []
        execute_queries = []
    
        execute_queries.append(state_result)
        key_values.append("result")
     
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

      


        




