from application.app_v1.database import get_db,get_db2
import json
from datetime import datetime
# Get wards
def getWardbadge(state,lga):
    with get_db() as conn:
        cur = conn.cursor()

        if state and lga:
            sql = f"""SELECT DISTINCT state_id, lga_id, ward_id ,ward_name FROM pu_result_table WHERE 
            state_id = {state} AND 
            lga_id = {lga}"""
        else:
            sql = "SELECT DISTINCT state_id, lga_id, ward_id ,ward_name FROM pu_result_table"

        try:
            cur.execute(sql)
            results = cur.fetchall()
               #cur.close()
            json_data1 = []
            json_data2 = []
            for row in results:
                sql = f"""SELECT COUNT(*) as  count1 FROM userdata_ward WHERE file_type=0 AND state_id = {state} AND lga_id = {lga} AND ward_id = {row['ward_id']}"""
                cur.execute(sql)
                row['images'] = cur.fetchone()
                sql = f"""SELECT COUNT(*) as  count1 FROM userdata_ward WHERE file_type=1 AND state_id = {state} AND lga_id = {lga} AND ward_id=  {row['ward_id']}"""
                cur.execute(sql)
                row['videos'] = cur.fetchone()
                json_data1.append(row['ward_id'])
                json_data2.append(row['ward_name'])
            return [json_data1]+[json_data2]+[results]
        except Exception as e:
            print("error in ward", state,lga, e)
            return str(e)



# Get wards
def getWard(state_id,lga_id):
    with get_db() as conn:
        cur = conn.cursor()

        if state_id and lga_id:
            sql = f"""SELECT DISTINCT state_id, lga_id, ward_id ,ward_name FROM pu_result_table WHERE 
            state_id = {state_id} AND 
            lga_id = {lga_id}"""
        else:
            sql = "SELECT DISTINCT state_id, lga_id, ward_id ,ward_name FROM pu_result_table"

        try:
            cur.execute(sql)
            results = cur.fetchall()
                #cur.close()
            json_data1 = []
            json_data2 = []
            for row in results:
                json_data1.append(row['ward_id'])
                json_data2.append(row['ward_name'])
            return [json_data1]+[json_data2]+[results]
        except Exception as e:
            print("error in ward", state_id,lga_id, e)
            return str(e)
    
# Get wards
def getdistrict(state_id,lga_id):
    with get_db() as conn:
        cur = conn.cursor()

        if state_id and lga_id:
            sql = f"""SELECT DISTINCT state_id,state_name, district_id,district_name FROM sen_pu_table WHERE 
            state_id = {state_id} AND 
            lga_id = {lga_id}"""
        # else:
        #     sql = "SELECT DISTINCT state_id, lga_id, ward_id ,ward_name FROM pu_result_table"

        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            
            json_data1 = []
            json_data2 = []
            for row in results:
                json_data1.append(row['DISTRICT_ID'])
                json_data2.append(row['DISTRICT_NAME'])
            return [json_data1]+[json_data2]+[results]
        except Exception as e:
            print("error in ward", state_id,lga_id, e)
            return str(e)

# Get wards
def getconstituency(state_id,lga_id):
    with get_db() as conn:
        cur = conn.cursor()

        if state_id and lga_id:
            sql = f"""SELECT DISTINCT state_id, state_name,house_id,house_name FROM house_pu_table WHERE 
            state_id = {state_id} AND 
            lga_id = {lga_id}"""
        # else:
        #     sql = "SELECT DISTINCT state_id, lga_id, ward_id ,ward_name FROM pu_result_table"

        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            
            json_data1 = []
            json_data2 = []
            for row in results:
                json_data1.append(row['house_id'])
                json_data2.append(row['house_name'])
            return [json_data1]+[json_data2]+[results]
        except Exception as e:
            print("error in ward", state_id,lga_id, e)
            return str(e)

# Get wards
def getWardsenate(state_name,senate_district,lga_name):
    with get_db() as conn:
        cur = conn.cursor()

  
        sql = f"SELECT DISTINCT state_id, state_name, district_id, district_name,lga_id, lga_name, ward_id ,ward_name FROM sen_pu_table WHERE  state_id={state_name} and district_id={senate_district} and lga_id= {lga_name}"

        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            
            json_data1 = []
            json_data2 = []
            res= {}
            for row in results:
                json_data1.append(row['ward_id'])
                json_data2.append(row['ward_name'])
            res['ward_id'] = json_data1
            res['ward_name'] = json_data2
            return [json_data1] +[json_data2] + [results]
        except Exception as e:
            print("error in ward", state_name,senate_district, e)
            return str(e)

# Get wards
def getWardrep(state_name,house_name,lga_name):
    with get_db() as conn:
        cur = conn.cursor()

  
        sql = f"SELECT DISTINCT  state_id, state_name,house_id,house_name, lga_id, lga_name,ward_id ,ward_name FROM house_pu_table WHERE  state_id={state_name} and house_id={house_name} and lga_id= {lga_name}"

        try:
            cur.execute(sql)
            results = cur.fetchall()
           
            
            json_data1 = []
            json_data2 = []
            res= {}
            for row in results:
                json_data1.append(row['ward_id'])
                json_data2.append(row['ward_name'])
            res['ward_id'] = json_data1
            res['ward_name'] = json_data2
            return [json_data1] +[json_data2] +[results]
        except Exception as e:
            print("error in ward", state_name,house_name, e)
            return str(e)



# Get ward
def getWardResult(country_name,state_name,lga_name,ward_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM ward_result_table where  state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name}"""
        sql1 = f"SELECT * FROM userdata_ward WHERE  state_id = {state_name} AND lga_id= {lga_name} AND ward_id = {ward_name}"

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
        




def getWardResultsenate(country_name,state_name,senate_district,lga_name,ward_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM sen_ward_table where  state_id= {state_name} and district_id={senate_district} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql1 = f"SELECT * FROM userdata_ward WHERE  state_id = {state_name} AND lga_id= {lga_name} AND ward_id = {ward_name}"

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

def getWardResultrep(country_name,state_name,house_name,lga_name,ward_name):
    with get_db() as conn:
        cur = conn.cursor()
        sql = f"""SELECT * FROM house_ward_table where  state_id= {state_name} and house_id={house_name} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql1 = f"SELECT * FROM userdata_ward WHERE  state_id = {state_name} AND lga_id= {lga_name} AND ward_id = {ward_name}"

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



def updateWardResult(country_name,state_name,lga_name,ward_name, data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update ward_result_table SET {query} , date_time ='{timer}',status='collated' where  state_id= {state_name} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql2 = f"""Select * from ward_result_table Where   state_id= {state_name} and lga_id = {lga_name}  and ward_id = {ward_name}"""
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

def updateWardResultsenate(country_name,state_name,senate_district,lga_name,ward_name,data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update sen_ward_table SET {query} , date_time ='{timer}',status='collated' where  state_id= {state_name} and district_id ={senate_district} and lga_id = {lga_name} and ward_id = {ward_name}"""
        sql2 = f"""Select * from sen_ward_table Where  state_id= {state_name} and district_id ={senate_district} and lga_id = {lga_name} and ward_id = {ward_name}"""
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

def updateWardResultrep(country_name,state_name,house_name,lga_name,ward_name, data={}):
    now = datetime.now() 
    with get_db() as conn:
        cur = conn.cursor()
      

        timer = now.strftime("%m/%d/%Y, %H:%M:%S")
        query = [
            f"{key}={value[0] if isinstance(value, list) else value}" for key, value in data.items()]
        query = query[:-1]
        query = ", ".join(query)
        sql = f"""Update house_ward_table SET {query} , date_time ='{timer}',status='collated' where  state_id= {state_name} and house_id ={house_name} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql2 = f"""Select * from house_ward_table Where  state_id= {state_name} and house_id ={house_name} and lga_id = {lga_name} and ward_id = {ward_name}"""
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


def cancelWardResult(country_name,state_name,lga_name,ward_name, data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update ward_result_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0,Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}'  where  state_id= {state_name} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql2 = f"""Select * FROM ward_result_table  where  state_id= {state_name} and lga_id = {lga_name} and ward_id = {ward_name}"""
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


def cancelWardResultsenate(country_name,state_name,senate_district,lga_name,ward_name,data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update sen_ward_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}' where state_id= {state_name}  and district_id={senate_district} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql2 = f"""Select * FROM sen_ward_table  Where  state_id= {state_name} and district_id={senate_district} and lga_id = {lga_name}  and ward_id = {ward_name}"""
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


def cancelWardResultsrep(country_name,state_name,house_name,lga_name,ward_name,data={}):
    now = datetime.now() 

    with get_db() as conn:
        cur = conn.cursor()
        timer = now.strftime("%m/%d/%Y, %H:%M:%S")

        sql = f"""Update house_ward_table SET status='canceled', A=0, AA=0, AAC=0, ADC=0, ADP=0, APC=0, APGA=0, APM=0, APP=0, BP=0, LP=0, NNPP=0, NRM=0, PDP=0, PRP=0, SDP=0, Total_Accredited_voters=0, Total_Rejected_votes=0, Total_Registered_voters=0,total_valid_votes_c=0, YPP=0, ZLP=0 , date_time ='{timer}' where  state_id= {state_name}  and house_id ={house_name} and lga_id = {lga_name}  and ward_id = {ward_name}"""
        sql2 = f"""Select * FROM house_ward_table  Where  state_id= {state_name} and house_id ={house_name} and lga_id = {lga_name}  and ward_id = {ward_name} """
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
