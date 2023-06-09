


from application.app_v1.database import get_db,get_db
import json
from datetime import datetime

# Get lga
def getLGAbadge(state_id):
    with get_db() as conn:
        cur = conn.cursor()
    
        if state_id:
            sql = f"SELECT DISTINCT state_id, lga_id, lga_name FROM pu_result_table WHERE  state_id = {state_id}"
        else: 
            sql = "SELECT DISTINCT state_id, lga_id, lga_name FROM pu_result_table"
        

        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            
            json_data1 = []
            json_data2 = []
            for row in results:
                sql = f"""SELECT COUNT(*) as  count1 FROM userdata_lga WHERE file_type=0 AND state_id = {state_id} AND lga_id = {row['lga_id']}"""
                cur.execute(sql)
                row['images'] = cur.fetchone()
                sql = f"""SELECT COUNT(*) as  count1 FROM userdata_lga WHERE file_type=1 AND state_id = {state_id} AND lga_id  = {row['lga_id']}"""
                cur.execute(sql)
                row['videos'] = cur.fetchone()
                json_data1.append(row['lga_id'])
                json_data2.append(row['lga_name'])
            return [json_data1]+[json_data2]+[results]
        except Exception as e:
            print("error in lga", state_id, e)
            return str(e)

def getLGA(state_name):
    with get_db() as conn:
        cur = conn.cursor()

        if state_name:
            sql = f"SELECT DISTINCT state_id, lga_id, lga_name FROM pu_result_table WHERE  state_id = {state_name}"
   
        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            json_data1 = []
            json_data2 = []
            for row in results:
                json_data1.append(row['lga_id'])
                json_data2.append(row['lga_name'])
            return [json_data1]+[json_data2]+[results]
        except Exception as e:
            print("error in lga", state_name, e)
            return str(e)

def getLGASenate(state_name,senate_district):
    with get_db() as conn:
        cur = conn.cursor()
     

    
        sql = f"SELECT DISTINCT state_id, state_name, district_id, district_name,lga_id, lga_name FROM sen_pu_table where state_id={state_name} and district_id={senate_district}"
        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            json_data1 = []
            json_data2 = []
            res = {}
            for row in results:
                json_data1.append(row['lga_id'])
                json_data2.append(row['lga_name'])
            res['lga_id'] = json_data1
            res['lga_name'] =json_data2
            return [json_data1] +[json_data2] + [results]
        except Exception as e:
            print("error in lga", state_name, e)
            return str(e)


def getLGArep(state_name,house_name):
    with get_db() as conn:
        cur = conn.cursor()
     

    
        sql = f"SELECT DISTINCT state_id, state_name,house_id,house_name, lga_id, lga_name FROM house_pu_table where state_id={state_name} and house_id={house_name}"
        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            json_data1 = []
            json_data2 = []
            res = {}
            for row in results:
                json_data1.append(row['lga_id'])
                json_data2.append(row['lga_name'])
            res['lga_id'] = json_data1
            res['lga_name'] =json_data2
            return [json_data1] +[json_data2] +[results]
        except Exception as e:
            print("error in lga", state_name, e)
            return str(e)

# Get Lga
def getLgaResult(country_name,state_name,lga_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM lga_result_table where  state_id= {state_name}  and lga_id = {lga_name}"""
        sql1 = f"SELECT * FROM userdata_lga WHERE  state_id = {state_name} AND lga_id= {lga_name}"

        final ={}
        try:
            cur.execute(sql)

            results = cur.fetchall()
           
            
            cur.execute(sql1)
            results1 = cur.fetchall()
   
            parties = ["A","AA","AAC","ADC","ADP","APC","APGA","APM","APP","BP","LP","NNPP","NRM","PDP","PRP","SDP","YPP","ZLP"]
            total =["Total_Accredited_voters","Total_Registered_voters","Total_Rejected_votes","total_valid_votes_c"]    
    
            data = ['date_time', 'person_collated']
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
    


def getLgaResultsenate(country_name,state_name,senate_district,lga_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM sen_lga_table where  state_id= {state_name}  and district_id={senate_district} and lga_id = {lga_name}"""
        sql1 = f"SELECT * FROM userdata_lga WHERE  state_id = {state_name} AND lga_id= {lga_name}"

        final ={}
        try:
            cur.execute(sql)

            results = cur.fetchall()
           
            
            cur.execute(sql1)

            results1 = cur.fetchall()
        
            parties = ["A","AA","AAC","ADC","ADP","APC","APGA","APM","APP","BP","LP","NNPP","NRM","PDP","PRP","SDP","YPP","ZLP"]
            total =["Total_Accredited_voters","Total_Registered_voters","Total_Rejected_votes","total_valid_votes_c"]    
    
            data = ['date_time', 'person_collated']
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

def getLgaResultrep(country_name,state_name,house_name,lga_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM house_lga_table where  state_id= {state_name}  and house_id={house_name} and lga_id = {lga_name}"""
        sql1 = f"SELECT * FROM userdata_lga WHERE  state_id = {state_name} AND lga_id= {lga_name}"

        final ={}
        try:
            cur.execute(sql)

            results = cur.fetchall()
           
            
            cur.execute(sql1)

            results1 = cur.fetchall()
          
            parties = ["A","AA","AAC","ADC","ADP","APC","APGA","APM","APP","BP","LP","NNPP","NRM","PDP","PRP","SDP","YPP","ZLP"]
            total =["Total_Accredited_voters","Total_Registered_voters","Total_Rejected_votes","total_valid_votes_c"]    
    
            data = ['date_time', 'person_collated']
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












def updateLgaResult(country_name,state_name,lga_name,  data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update lga_result_table SET {query} , date_time ='{timer}',status='collated' where  state_id= {state_name}  and lga_id = {lga_name}"""
        sql2 = f"""Select * from lga_result_table Where   state_id= {state_name}  and lga_id = {lga_name}"""
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



def updateLgaResultsenate(country_name,state_name,senate_district,lga_name,data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update sen_lga_table SET {query} , date_time ='{timer}',status='collated' where  state_id= {state_name}  and district_id ={senate_district} and lga_id = {lga_name}"""
        sql2 = f"""Select * from sen_lga_table Where  state_id= {state_name}  and district_id ={senate_district} and lga_id = {lga_name}"""
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


def updateLgaResultrep(country_name,state_name,house_name,lga_name,data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update house_lga_table SET {query} , date_time ='{timer}',status='collated' where  state_id= {state_name}  and house_id ={house_name} and lga_id = {lga_name}"""
        sql2 = f"""Select * from house_lga_table Where  state_id= {state_name}  and house_id ={house_name} and lga_id = {lga_name}"""
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




def cancelLgaResult(country_name,state_name,lga_name, data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update lga_result_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 ,date_time ='{timer}'  where  state_id= {state_name}  and lga_id = {lga_name}"""
        sql2 = f"""Select * FROM lga_result_table where  state_id= {state_name}  and lga_id = {lga_name} """
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






def cancelLgaResultsenate(country_name,state_name,senate_district,lga_name,data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update sen_lga_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}' where state_id= {state_name}  and district_id ={senate_district} and lga_id = {lga_name}"""
        sql2 = f"""Select * FROM sen_lga_table  Where  state_id= {state_name}  and district_id ={senate_district} and lga_id = {lga_name}"""
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




def cancelLgaResultsrep(country_name,state_name,house_name,lga_name,data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update house_lga_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}' where  state_id= {state_name}  and house_id ={house_name} and lga_id = {lga_name}"""
        sql2 = f"""Select * FROM house_lga_table  Where  state_id= {state_name}  and house_id ={house_name} and lga_id = {lga_name} """
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






