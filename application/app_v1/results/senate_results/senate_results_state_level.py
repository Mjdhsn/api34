from application.app_v1.database import get_db,get_db2
from application.app_v1.results.senate_results.partytable import presidential_table_state
import json





# state results

def get_state_state_all_results(country_name="undefined",state_name="undefined",district_name="undefined"):
       with get_db2() as conn:
        cur = conn.cursor()

         
        country_query = ""
        state_query = ""
        district_query =""

      

     
        final_results = {}
        if country_name and country_name != "undefined":
            country_query = f" AND country_id ={country_name}"
        if state_name and state_name != "undefined":
            state_query = f" AND state_id={state_name}"
        if district_name and district_name != "undefined":
            district_query = f" AND district_id={district_name}"
       
      

        state_result = f"""{presidential_table_state['query']} select district_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
     	  Total_Registered_voters,  total_valid_votes_c AS total_valid_votes, Total_Rejected_votes, total_votes_cast_c AS total_vote_casted FROM dist where 1=1 {state_query} ORDER BY district_id """
        key_values = []
        execute_queries = []
        execute_queries.append(state_result)
        key_values.append("result")

        map1 = ['STATE_NAME']
        map2 = ['TOTAL_REGISTERED_VOTERS','TOTAL_ACCREDITED_VOTERS','TOTAL_REJECTED_VOTES']
        map3 = ['REMARKS']
        result = ['result']
        mapres =['STATE_NAME']
        query =[]
        for index,sql in enumerate(execute_queries):
                try:
                    cur.execute_async(sql)
                    query.append(cur.sfqid)
                except:
                    print('Skipped a sceanrio')
        ress = {}
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
        return ress

        

       