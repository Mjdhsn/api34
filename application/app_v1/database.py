import pymysql
import snowflake.connector


HOST = 'electionkanoml.cypjjjls3xgo.eu-west-1.rds.amazonaws.com'
# HOST ='election.cypjjjls3xgo.eu-west-1.rds.amazonaws.com'
USER = 'admin'
PASS = 'election1234'
db='KANO'



def get_db():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASS,
        db=db,
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

# def get_db():
#     return snowflake.connector.connect(

#     user= 'ismail',
#     password = 'Ismail01?',
#     account = 'wagtiji-ky72580',
#     database='DATA',
#     schema = 'PUBLIC',
#     warehouse='TEST'
# )

# def get_db():
#     return snowflake.connector.connect(

#     user= 'sjdhsn',
#     password = 'Sjdhsn.567',
#     account = 'vozrhej-ym73300',
#     database='DATA',
#     schema = 'PUBLIC',
#     warehouse='TEST'
# )

# def get_db():
#     return snowflake.connector.connect(

#     user= 'jameel',
#     password = 'Jamilu01?',
#     account = 'pgvbhpz-jq78554',
#     database='MYDATA',
#     schema = 'PUBLIC',
#     warehouse='MYTEST'
# )


# def get_db():
#     return snowflake.connector.connect(

#     user= 'lawan',
#     password = 'Lawan01?',
#     account = 'lidnpuk-vn41998',
#     database='MYTRIAL',
#     schema = 'PUBLIC',
#     warehouse='TRIAL',
# )

# def get_db():
#     return snowflake.connector.connect(

#     user= 'maryam',
#     password = 'Maryam01?',
#     account = 'lwvnpeb-td66940',
#     database='MYTEST',
#     schema = 'PUBLIC',
#     warehouse='TEST',
# )


# def get_db():
#     return snowflake.connector.connect(

#     user= 'hassana',
#     password = 'Hassana01?',
#     account = 'qgjflwi-yo31754',
#     database='MYTEST',
#     schema = 'PUBLIC',
#     warehouse='TEST',
# )


#def get_db():
#    return snowflake.connector.connect(

#    user= 'hafsa',
#    password = 'Hafsa01?',
#    account = 'mqnguim-ll14025',
#    database='MYTRIAL',
#    schema = 'PUBLIC',
#    warehouse='TRIAL',
#)


# def get_db():
#     return snowflake.connector.connect(

#     user= 'maryam',
#     password = 'Maryam01?',
#     account = 'yloufpv-js63877',
#     database='LOGEECAI',
#     schema = 'PUBLIC',
#     warehouse='LOGEEC',
# )



def get_db2():
    return snowflake.connector.connect(

    user= 'majid',
    password = 'Mjdhsn.567',
    account = 'atcdeci-fu15130',
    database='DATA',
    schema = 'PUBLIC',
    warehouse='TEST',
)