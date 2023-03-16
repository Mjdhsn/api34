
from app.application.app_v1.database import get_db,get_db2
import json
from datetime import datetime


# def addData_all(role,country,state, lga, ward, pu, file, remark, type, lat, long, phone, email):


import re
import difflib
def ai(user,image):
    user_data = user['user']
    role_input = user_data['role']
    level_input = user_data['level_childs']
    name = user_data['name']
    aspirant_photo = user_data['aspirant_avatar']
    typo =user_data['type_of_election'] 
    # now = datetime.now() 
  
    with get_db() as conn:
        cur = conn.cursor()
        if role_input == "pns":
            country_name = level_input['country']
            now = datetime.now() 

            timer = now.strftime("%m/%d/%Y %H:%M")
            pass
        
        elif role_input == "pss":
            country_name = level_input['country']
            state_name = level_input['state']
            timer = now.strftime("%m/%d/%Y %H:%M")
       
            pass
        
                
        elif role_input == "pls":
            country_name = level_input['country']
            state_name = level_input['state']
            lga_name = level_input['lga']
            timer = now.strftime("%m/%d/%Y %H:%M")

            pass

        elif role_input == "pws":
            country_name = level_input['country']
            state_name = level_input['state']
            lga_name = level_input['lga']
            ward_name = level_input['ward']
            timer = now.strftime("%m/%d/%Y %H:%M")

            pass
   

        elif role_input == "ppa":
            country_name = level_input['country']
            state_name = level_input['state']
            lga_name = level_input['lga']
            ward_name = level_input['ward']
            pu_name = level_input['pollingUnit']
            timer = now.strftime("%m/%d/%Y %H:%M")
            
            sql = f"""Update pu_result_table SET {query} , date_time ='{timer}',status='collated' where country_id= {country_name} AND state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
            sql2 = f"""Select * from pu_result_table Where country_id= {country_name} AND  state_id = {state_name} and lga_id = {lga_name} and ward_id = {ward_name} and pu_id= {pu_name}"""
        
           
        
        elif role_input == "sds":
            country_name = level_input['country']
            district_name = level_input['district']
            state_name = level_input['state']
            timer = now.strftime("%m/%d/%Y %H:%M")
            pass
            




        elif role_input == "spa":
            country_name = level_input['country']
            state_name = level_input['state']
            district_name = level_input['district']
            lga_name = level_input['lga']
            ward_name = level_input['ward']
            pu_name = level_input['pollingUnit']
            timer = now.strftime("%m/%d/%Y %H:%M")

            pass

        elif role_input == "rcs":
            country_name = level_input['country']
            constituency_name = level_input['constituency']
            state_name = level_input['state']
            timer = now.strftime("%m/%d/%Y %H:%M")
            pass


def addData_pu(state, lga, ward, pu, file, remark, type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_pu
                    (
                    state_name,
                    lga_name,
                   ward_name,
                   pu_name,
                   remark,
                   
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, % s, % s, % s, %s,%s, %s)'''
                    
            cur.execute(
                sql, (state, lga, ward, pu,  remark, file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'

def getData_pu(country,state, lga, ward, pu):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_pu WHERE  state_id = {state} AND lga_id= {lga} AND ward_id = {ward} AND pu_id = {pu}"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()

            # cur.close()
            json_data = results
            return json_data
        except Exception as e:
            print(e)
            return str(e)



def addData_ward(state, lga, ward,file, remark, type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_ward
                    (
                    state_name,
                    lga_name,
                   ward_name,
                   remark,               
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, % s, % s, %s,%s,%s)'''
                    
            cur.execute(
                sql, (state, lga, ward,  remark, file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'


def getData_ward(country,state, lga, ward):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_ward WHERE  state_id = {state} AND lga_id= {lga} AND ward_id = {ward}"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()

            # cur.close()
            json_data = results

            # cur.close()
            return json_data
        except Exception as e:
            print(e)
            return str(e)


def addData_lga(state, lga,file, remark, type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_lga
                    (
                    state_name,
                    lga_name,
                   remark,
                   
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, %s,%s, %s, %s)'''
                    
            cur.execute(
                sql, (state, lga, remark, file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'


def getData_lga(country,state, lga):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_lga WHERE  state_id = {state} AND lga_id= {lga}"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()
        

            # cur.close()
            json_data = results
            return json_data
        except Exception as e:
            print(e)
            return str(e)

def addData_district(state, district, file, remark, type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_district
                    (
                    state_name,
                    district_name,
                   remark,
                   
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, % s, %s,%s, %s)'''
                    
            cur.execute(
                sql, (state, district, remark, file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'


def getData_district(country,state, constituency):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_district WHERE  state_id = {state} AND district_id= {constituency}"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()


            # cur.close()
            json_data = results
            return json_data
        except Exception as e:
            print(e)
            return str(e)

def addData_constituency(state, constituency, file, remark, type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_constituency
                    (
                    state_name,
                    constituency_name,
                   remark,
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, % s, %s,%s, %s)'''
                    
            cur.execute(
                sql, (state, constituency, remark, file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'


def getData_constituency(country,state, constituency):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_constituency WHERE  state_id = {state} AND house_id = {constituency}"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()

            

            # cur.close()
            json_data = results
            return json_data
        except Exception as e:
            print(e)
            return str(e)


def addData_state(state,file, remark, type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_state
                    (
                    state_name,
                   remark,
                   
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, %s,%s, %s)'''
                    
            cur.execute(
                sql, (state, remark,file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'


def getData_state(country,state):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_state WHERE state_id ={state}"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()
            # cur.close()
            json_data = results
            return json_data
        except Exception as e:
            print(e)
            return str(e)


def addData_country(country,file, remark,type, lat, long, phone, email ):
    with get_db() as conn:
        cur = conn.cursor()
        try:
            sql = '''INSERT INTO userdata_country
                    (country,
                   remark,
                   
                   file,
                    file_type,
                    lat,
                    long,
                    phone,
                     email

                    )
                    VALUES(% s, % s, % s, % s, % s, %s,%s, %s)'''
                    
            cur.execute(
                sql, (country,remark, file, type, lat, long, phone, email))
            conn.commit()
        # app.conn.close()
            return '1'
        except:
            return '0'


#needs to be updated

def getData_country(country):

    with get_db() as conn:
        cur = conn.cursor()

        sql = f"SELECT * FROM userdata_country"
        try:
            cur.execute(sql)
            row_headers = [x[0] for x in cur.description]
            results = cur.fetchall()
            # cur.close()
            json_data = results
            return json_data
        except Exception as e:
            print(e)
            return str(e)
