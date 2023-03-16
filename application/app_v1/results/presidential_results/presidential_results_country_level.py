from app.application.app_v1.database import get_db,get_db2
from app.application.app_v1.results.presidential_results.partytable import presidential_table_country
import json





def get_country_country_all_results(data={}):
    with get_db2() as conn:
        cur = conn.cursor()
      
        
        country_result = f"""{presidential_table_country['query']}  select country_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
		 Total_Registered_voters,  total_valid_votes_c AS total_valid_votes, Total_Rejected_votes, total_votes_cast_c AS total_vote_casted,remarks from ct"""

        final_results = {}

   

        keys = ['result']


        all_lists = [country_result]
            
    
        try:
            for index, val in enumerate(all_lists):
                cur.execute(val)
                # val_results = cur.fetchall()
                val_results = cur.fetch_pandas_all()
                val_results = val_results.to_json(orient="records")
                val_results = json.loads(val_results)
                final_results[keys[index]] = val_results
            return final_results
        except Exception as e:
            print(e)
            return str(e)






