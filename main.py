#Twitter: Bek Brace
#Instagram: Bek Brace

import uvicorn
from fastapi import FastAPI, Body, Depends,HTTPException, Security,Form
import random
from requests.structures import CaseInsensitiveDict
from fastapi.middleware.cors import CORSMiddleware
import json, requests
from fastapi import FastAPI, Request
from typing import Optional
from application.app_v1.model import UserLoginSchema

from fastapi import File, UploadFile
from application.app_v1.model import Model
import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from application.app_v1.collation.presidential_collation import country,state,lga,ward,polling_unit
from application.app_v1.mobile import mobile,upload_data
from application.app_v1.results.presidential_results import presidential_results_polling_unit_level,presidential_results_ward_level,presidential_results_lga_level,presidential_results_state_level,presidential_results_country_level
from application.app_v1.analysis.presidential_analysis.tab1 import presidential_analysis_polling_unit_level,presidential_analysis_ward_level,presidential_analysis_lga_level,presidential_analysis_state_level,presidential_analysis_country_level
from application.app_v1.analysis.presidential_analysis.tab3_copy import presidential_analysis_polling_unit_level_prediction,presidential_analysis_ward_level_prediction,presidential_analysis_lga_level_prediction,presidential_analysis_state_level_prediction,presidential_analysis_country_level_prediction
from application.app_v1.analysis.presidential_analysis.tab2_copy import presidential_analysis_polling_unit_level_party,presidential_analysis_ward_level_party,presidential_analysis_state_level_party,presidential_analysis_country_level_party,presidential_analysis_lga_level_party
# ,presidential_analysis_ward_level_party,presidential_analysis_lga_level_party,presidential_analysis_state_level_party,presidential_analysis_country_level_party
from application.app_v1.comparism.presidential import presidential_analysis_country_level_comparism,presidential_analysis_lga_level_comparism,presidential_analysis_state_level_comparism,presidential_analysis_ward_level_comparism
from mangum import Mangum
from application.app_v1.analysis.senate_analysis.tab1 import senate_analysis_country_level,senate_analysis_lga_level,senate_analysis_polling_unit_level,senate_analysis_state_level,senate_analysis_ward_level
from application.app_v1.results.senate_results import senate_results_country_level,senate_results_lga_level,senate_results_polling_unit_level,senate_results_ward_level,senate_results_state_level
from application.app_v1.analysis.rep_analysis.tab1 import rep_analysis_country_level,rep_analysis_lga_level,rep_analysis_polling_unit_level,rep_analysis_state_level,rep_analysis_ward_level
from application.app_v1.results.rep_results import  rep_results_country_level,rep_results_lga_level,rep_results_polling_unit_level,rep_results_state_level,rep_results_ward_level

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from application.app_v1.auth.auth import Auth

from fastapi_jwt import (
    JwtAccessBearerCookie,
    JwtAuthorizationCredentials,
    JwtRefreshBearer,
)
from datetime import timedelta

app = FastAPI()


origins = ["*"]
security = HTTPBearer()
auth_handler = Auth()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Read access token from bearer header and cookie (bearer priority)
access_security = JwtAccessBearerCookie(
    secret_key="$8885%$*@95949459@@@@",
    auto_error=False,
    access_expires_delta=timedelta(hours=2000)  # change access token validation timedelta
)
# Read refresh token from bearer header only
refresh_security = JwtRefreshBearer(
    secret_key="463849505##@$%#$", 
    auto_error=True  # automatically raise HTTPException: HTTP_401_UNAUTHORIZED 
)

@app.post("/token", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    #  user_data = user_managment.authenticate(user.email, user.password)
     subject = {"username":user.email , "role": "user"}
    #  if user.email != user_data['email'] or user.password != user_data['passcode']:
    #              raise HTTPException(status_code=401,detail="Bad username or password")
     # Create new access/refresh tokens pair
     access_token = access_security.create_access_token(subject=subject)
     refresh_token = refresh_security.create_refresh_token(subject=subject)

    #  access_token = auth_handler.encode_token(str(user.email))
    #  refresh_token = auth_handler.encode_refresh_token(user.email)
    #  access_token = signJWT(user.email)
     response = {"message": 'login successful',
                    "access_token": access_token,'refresh_token': refresh_token}
     return response


    
# 
@app.get('/refresh',tags=["user"])
def refresh_token( credentials: JwtAuthorizationCredentials = Security(refresh_security)):
    # refresh_token = credentials.credentials
    access_token = access_security.create_access_token(subject=credentials.subject)
    refresh_token = refresh_security.create_refresh_token(subject=credentials.subject, expires_delta=timedelta(days=50))
    # new_token = auth_handler.refresh_token(refresh_token)
    {"access_token": access_token, "refresh_token": refresh_token}

# @app.delete('/logout',tags=["user"])
# def logout(Authorize: AuthJWT = Depends()):
#     """
#     Because the JWT are stored in an httponly cookie now, we cannot
#     log the user out by simply deleting the cookies in the frontend.
#     We need the backend to send us a response to delete the cookies.
#     """
#     Authorize.jwt_required()
    
#     Authorize.unset_jwt_cookies()
#     return {"msg":"Successfully logout"}


# @app.get("/getCountry", tags=["dropdowns"])
# def getCountry(credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
   
#     return country.getCountry()


@app.get("/getState", tags=["dropdowns"])
def getState(credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
   

    return state.getState()


@app.get("/getLGA", tags=["dropdowns"])
def getLGA(state_name:  int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.getLGA(state_name)


''' Ward '''
@app.get("/getWard", tags=["dropdowns"])
def getWard(state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.getWard(state_name,lga_name)
  
# ''' District '''
# @app.get("/getDistrictvalue", tags=["dropdowns"])
# def getWard(state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return ward.getdistrict(state_name,lga_name)
  

''' Constituency '''
@app.get("/getconstituencyvalue", tags=["dropdowns"])
def getWard(state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.getconstituency(state_name,lga_name)

@app.get("/getPol", tags=["dropdowns"])
def getPol(state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.getPollingUnit(state_name, lga_name,ward_name)

#####################


# @app.get("/getSenateState", tags=["dropdowns for senates"])
# def getState(credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
   

#     return state.getState()

# @app.get("/getSenateDistricts", tags=["dropdowns for senates"])
# def getState(state_name:  int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
   

#     return state.getStateSenate(state_name)


# @app.get("/getSenateLGA", tags=["dropdowns for senates"])
# def getLGA(state_name:  int = 19,senate_district:  int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return lga.getLGASenate(state_name,senate_district)


# ''' Ward '''
# @app.get("/getSenateWard", tags=["dropdowns for senates"])
# def getWard(state_name:  int = 19,senate_district:  int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return ward.getWardsenate(state_name,senate_district,lga_name)
  


# @app.get("/getSenatePol", tags=["dropdowns for senates"])
# def getPol(state_name:  int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return polling_unit.getPollingUnitsenate(state_name, senate_district,lga_name,ward_name)



@app.get("/getRepState", tags=["dropdowns for Rep"])
def getState(credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
   

    return state.getState()

@app.get("/getRepConstituency", tags=["dropdowns for Rep"])
def getState(state_name:  int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
   

    return state.getStaterep(state_name)


@app.get("/getRepLGA", tags=["dropdowns for Rep"])
def getLGA(state_name:  int = 19,constituency_name:  int = 499,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.getLGArep(state_name,constituency_name)


''' Ward '''
@app.get("/getRepWard", tags=["dropdowns for Rep"])
def getWard(state_name:  int = 19,constituency_name:  int = 499,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.getWardrep(state_name,constituency_name,lga_name)
  


@app.get("/getRepPol", tags=["dropdowns for Rep"])
def getPol(state_name:  int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.getPollingUnitrep(state_name, constituency_name,lga_name,ward_name)



# '''Get values of badges'''

# # @app.get("/getCountrybadge", tags=["dropdowns with badges for Information"])
# # def getCountry(credentials: HTTPAuthorizationCredentials = Security(security)):
# #     if not credentials:
# #         raise HTTPException(status_code=401, detail='my-custom-details')

# #     return country.getCountrybadge()


# @app.get("/getStatebadge", tags=["dropdowns with badges for Information"])
# def getState(credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')

#     return state.getStatebadge()


# @app.get("/getSenatebadge", tags=["dropdowns with badges for Information"])
# def getSenate(state_name:  int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')

#     return state.getSenateebadge(state_name)


# @app.get("/getRepbadge", tags=["dropdowns with badges for Information"])
# def getRep(state_name:  int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')

#     return state.getRepebadge(state_name)


# @app.get("/getLGAbadge", tags=["dropdowns with badges for Information"])
# def getLGA(state_name:  int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')

#     return lga.getLGAbadge(state_name)


# ''' Ward '''
# @app.get("/getWardbadge", tags=["dropdowns with badges for Information"])
# def getWard(state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return ward.getWardbadge(state_name, lga_name)
  


# @app.get("/getPolbadge", tags=["dropdowns with badges for Information"])
# def getPol(state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return polling_unit.getPollingUnitbadge(state_name,lga_name,ward_name)


# '''....................................INFORMATIONS TAB BAR....................................'''

'''...............Pu data for Informations page..................'''

@app.get('/getDataPu',tags=["Informations"])
def getBook_pu(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,pu_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return upload_data.getData_pu(country_name,state_name, lga_name, ward_name, pu_name)



'''...............Ward data for Informations page..................'''

@app.get('/getData_ward',tags=["Informations"])
def getBook_ward(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return upload_data.getData_ward(country_name,state_name, lga_name, ward_name)
   

'''...............lga data for Informations page..................'''
@app.get('/getData_lga',tags=["Informations"])
def getBook_lga(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return upload_data.getData_lga(country_name,state_name, lga_name)

# '''...............districts data for Informations page..................'''
# @app.get('/getData_senateDistricts',tags=["Informations"])
# def getBook_district(country_name: int = 1,state_name: int = 19,senate_district: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return upload_data.getData_district(country_name,state_name, senate_district)  


'''...............constituencncy data for Informations page..................'''
@app.get('/getData_constituency',tags=["Informations"])
def getBook_constituency(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return upload_data.getData_constituency(country_name,state_name, constituency_name)  

'''...............state data for Informations page..................'''

@app.get('/getData_state',tags=["Informations"])
def getBook_state(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return upload_data.getData_state(country_name,state_name)



'''...............country data for Informations page..................'''

# @app.get('/getData_country',tags=["Informations"])
# async def getBook_country(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return upload_data.getData_country(country_name)



'''...............Pu data for coalation page..................'''
@app.get("/get-pu-result", tags=["Presidential polling unit collation"])
def getPUResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,pu_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.getPUResult(country_name, state_name,lga_name,ward_name,pu_name)


@app.post("/update-pu", tags=["Presidential polling unit collation"])
async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
    '''    


    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.updatePUResult(country_name, state_name,lga_name,ward_name,pu_name,data)

@app.post("/cancel-pu", tags=["Presidential polling unit collation"])
async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.cancelPUResult(country_name, state_name,lga_name,ward_name,pu_name,data)




# '''...............Pu data for senate coalation page..................'''
# @app.get("/get-sen-pu-result", tags=["Senate polling unit collation"])
# def getPUResult(country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,pu_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return polling_unit.getPUResultsenate(country_name, state_name,senate_district,lga_name,ward_name,pu_name)


# @app.post("/update-sen-pu", tags=["Senate polling unit collation"])
# async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

#     Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
#     '''    


#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return polling_unit.updatePUResultsenate(country_name, state_name,senate_district,lga_name,ward_name,pu_name,data)

# @app.post("/cancel-sen-pu", tags=["Senate polling unit collation"])
# async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

#     Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return polling_unit.cancelPUResultsenate(country_name, state_name,senate_district,lga_name,ward_name,pu_name,data)




'''...............Pu data for rep coalation page..................'''
@app.get("/get-rep-pu-result", tags=["Rep polling unit collation"])
def getPUResult(country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,pu_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.getPUResultrep(country_name, state_name,constituency_name,lga_name,ward_name,pu_name)


@app.post("/update-rep-pu", tags=["Rep polling unit collation"])
async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
    '''    


    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.updatePUResultrep(country_name, state_name,constituency_name,lga_name,ward_name,pu_name,data)

@app.post("/cancel-rep-pu", tags=["Rep polling unit collation"])
async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return polling_unit.cancelPUResultsrep(country_name, state_name,constituency_name,lga_name,ward_name,pu_name,data)







'''...............Ward data for coalation page..................'''
@app.get("/get-ward-result", tags=["Presidential Ward collation"])
def getWardResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name

     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.getWardResult(country_name, state_name,lga_name,ward_name)


@app.post("/update-ward", tags=["Presidential Ward collation"])
async def updateWardResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name,ward_name

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}

     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.updateWardResult(country_name, state_name,lga_name,ward_name,data)

@app.post("/cancel-ward", tags=["Presidential Ward collation"])
async def cancelWardResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name,ward_name


    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.cancelWardResult(country_name, state_name,lga_name,ward_name,data)


# '''...............Ward data for senate coalation page..................'''
# @app.get("/get-sen-ward-result", tags=["Senate Ward collation"])
# def getPUResult(country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,district,lga_name,ward_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return ward.getWardResultsenate(country_name, state_name,senate_district,lga_name,ward_name)


# @app.post("/update-sen-ward", tags=["Senate Ward collation"])
# async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,district,lga_name,ward_name

#     Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
#     '''    


#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return ward.updateWardResultsenate(country_name, state_name,senate_district,lga_name,ward_name,data)

# @app.post("/cancel-sen-ward", tags=["Senate Ward collation"])
# async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,district,lga_name,ward_name

#     Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return ward.cancelWardResultsenate(country_name, state_name,senate_district,lga_name,ward_name,data)


'''...............Ward data for rep coalation page..................'''
@app.get("/get-rep-ward-result", tags=["Rep Ward collation"])
def getPUResult(country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,constituency,lga_name,ward_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.getWardResultrep(country_name, state_name,constituency_name,lga_name,ward_name)


@app.post("/update-rep-ward", tags=["Rep Ward collation"])
async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,constituency,lga_name,ward_name

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
    '''    


    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.updateWardResultrep(country_name, state_name,constituency_name,lga_name,ward_name,data)

@app.post("/cancel-rep-ward", tags=["Rep Ward collation"])
async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,constituency,lga_name,ward_name

    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return ward.cancelWardResultsrep(country_name, state_name,constituency_name,lga_name,ward_name,data)




'''...............Lga data for coalation page..................'''
@app.get("/get-lga-result", tags=["Presidential Lga collation"])
def getLgaResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,lga_name

     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.getLgaResult(country_name, state_name,lga_name)


@app.post("/update-lga", tags=["Presidential Lga collation"])
async def updateLgaResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    
    '''
    Input params -  coutry_name,state_name


    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}

     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.updateLgaResult(country_name, state_name,lga_name,data)

@app.post("/cancel-lga", tags=["Presidential Lga collation"])
async def cancelLgaResult(country_name: int = 1,state_name: int = 19,lga_name: int = 1,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name


    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return lga.cancelLgaResult(country_name, state_name,lga_name,data)



# '''...............Lga data for senate coalation page..................'''
# @app.get("/get-sen-lga-result", tags=["Senate Lga collation"])
# def getPUResult(country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,district,lga_name,

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return lga.getLgaResultsenate(country_name, state_name,senate_district,lga_name)


# @app.post("/update-sen-lga", tags=["Senate Lga collation"])
# async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,district,lga_name

#     Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
#     '''    


#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return lga.updateLgaResultsenate(country_name, state_name,senate_district,lga_name,data)

# @app.post("/cancel-sen-lga", tags=["Senate Lga collation"])
# async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,district,lga_name

#     Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return lga.cancelLgaResultsenate(country_name, state_name,senate_district,lga_name,data)

'''...............Lga data for rep coalation page..................'''
@app.get("/get-rep-lga-result", tags=["Rep Lga collation"])
def getPUResult(country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,constituency,lga_name,

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.getLgaResultrep(country_name, state_name,constituency_name,lga_name)


@app.post("/update-rep-lga", tags=["Rep Lga collation"])
async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,constituency,lga_name

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
    '''    


    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.updateLgaResultrep(country_name, state_name,constituency_name,lga_name,data)

@app.post("/cancel-rep-lga", tags=["Rep Lga collation"])
async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,constituency,lga_name

    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return lga.cancelLgaResultsrep(country_name, state_name,constituency_name,lga_name,data)



'''...............State data for coalation page..................'''
@app.get("/get-state-result", tags=["Presidential State collation"])
def getStateResult(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
    '''
    
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return state.getStateResult(country_name,state_name)


@app.post("/update-state", tags=["Presidential State collation"])
async def updateStateResult(country_name: int = 1,state_name: int = 19,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return state.updateStateResult(country_name,state_name,data)

@app.post("/cancel-state", tags=["Presidential State collation"])
async def cancelStateResult(country_name: int = 1,state_name: int = 19,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name

    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}
     
    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return state.cancelStateResult(country_name, state_name,data)


# '''...............district data for senate coalation page..................'''
# @app.get("/get-sen-district-result", tags=["Senate district collation"])
# def getPUResult(country_name: int = 1,state_name: int = 19,senate_district:  int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,district

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return state.getStateResultsenate(country_name, state_name,senate_district)


# @app.post("/update-sen-district", tags=["Senate district collation"])
# async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,district

#     Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
#     '''    


#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return state.updateStateResultsenate(country_name, state_name,senate_district,data)

# @app.post("/cancel-sen-district", tags=["Senate district collation"])
# async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,senate_district:  int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name,state_name,district

#     Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return state.cancelStateResultsenate(country_name, state_name,senate_district,data)


'''...............constituency data for senate coalation page..................'''
@app.get("/get-rep-constituency-result", tags=["Rep constituency collation"])
def getPUResult(country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,constituency

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return state.getStateResultrep(country_name, state_name,constituency_name)


@app.post("/update-rep-constituency-district", tags=["Rep constituency collation"])
async def getupdatePUResultPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,constituency

    Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
    
     
    '''    


    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return state.updateStateResultrep(country_name, state_name,constituency_name,data)

@app.post("/cancel-rep-constituency", tags=["Rep constituency collation"])
async def cancelPUResult(data:dict= Body(...),country_name: int = 1,state_name: int = 19,constituency_name:  int = 499,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params -  coutry_name,state_name,constituency

    Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

    '''
    
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return state.cancelStateResultsrep(country_name, state_name,constituency_name,data)


# '''...............Country data for coalation page..................'''

# @app.get("/get-country-result", tags=["Presidential Country collation"])
# def getCountryResult(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name

     
#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return country.getCountryResult(country_name)


# @app.post("/update-country", tags=["Presidential Country collation"])
# async def updateCountryResult(country_name: int = 1,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name

#     Input request data - party check box data for example {"A": 0, "AA": ["4"], "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Rejected_votes": 0}
     
#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return country.updateCountryResult(country_name,data)

# @app.post("/cancel-country", tags=["Presidential Country collation"])
# async def cancelCountryResult(country_name: int = 1,data:dict= Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params -  coutry_name


#     Input request data - party check box data for example {"A": 0, "AA": 0, "AAC": 0, "ADC": 0, "ADP": 0, "APC": 0, "APGA": 0, "APM": 0, "APP": 0, "BP": 0, "LP": 0, "NNPP": 0, "NRM": 0, "PDP": 0, "PRP": 0, "SDP": 0, "YPP": 0, "ZLP": 0, "Total_Accredited_voters": 0,"Total_Registered_voters": ["500"], "Total_Registered_voters": 0, "Total_Rejected_votes": 0}

     
#     '''
    
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return country.cancelCountryResult(country_name,data)



'''............................Results Presidential elections ............................................'''

# Results presidential


# Polling page

@app.post("/presidentialresults_polling/ward",tags=["Presidential Polling Unit results"])
async def presidential_results_polling_ward_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_results_polling_unit_level.get__polling_ward_all_results(country_name,state_name, lga_name,ward_name)

@app.post("/presidentialresults_polling/lga",tags=["Presidential Polling Unit results"])
async def presidential_results_polling_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_results_polling_unit_level.get_polling_lga_all_results(country_name,state_name,lga_name)

@app.post("/presidentialresults_polling/state",tags=["Presidential Polling Unit results"])
async def presidential_results_polling_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_results_polling_unit_level.get_polling_state_all_results(country_name,state_name)

# @app.post("/presidentialresults_polling/country",tags=["Presidential Polling Unit results"])
# async def presidential_results_polling_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_results_polling_unit_level.get_polling_country_all_results(country_name)


# Ward



@app.post("/presidentialresults_ward/lga",tags=["Presidential Ward results"])
async def presidential_results_ward_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_results_ward_level.get_ward_lga_all_results(country_name,state_name,lga_name)

@app.post("/presidentialresults_ward/state", tags=["Presidential Ward results"])
async def presidential_results_ward_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_results_ward_level.get_ward_state_all_results(country_name,state_name)

# @app.post("/presidentialresults_ward/country",tags=["Presidential Ward results"])
# async def presidential_results_ward_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_results_ward_level.get_ward_country_all_results(country_name)



# Lga



@app.post("/presidentialresults_lga/state", tags=["Presidential LGA results"])
async def presidential_results_lga_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_results_lga_level.get_lga_state_all_results(country_name,state_name)

# @app.post("/presidentialresults_lga/country", tags=["Presidential LGA results"])
# async def presidential_results_lga_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):

#     '''

     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_results_lga_level.get_lga_country_all_results(country_name)

# State


@app.post("/presidentialresults_state/country", tags=["Presidential State results"])
async def presidential_results_state_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''

     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_results_state_level.get_state_country_all_results(country_name)

# # Country 
# @app.post("/presidentialresults_country/country", tags=["Presidential Country results"])
# async def presidential_results_country_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_results_country_level.get_country_country_all_results()
# '''...............................................................................................................'''



# """......................................................Results of Senate ........................................"""


# # Polling page

# @app.post("/senateresults_polling/ward",tags=["senate Polling Unit results"])
# async def senate_results_polling_ward_result(country_name: int = 1,state_name: int = 19,district_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,lga_name,ward_name

     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_polling_unit_level.get__polling_ward_all_results(country_name,state_name,district_name,lga_name,ward_name)

# @app.post("/senateresults_polling/lga",tags=["senate Polling Unit results"])
# async def senate_results_polling_lga_result(country_name: int = 1,state_name: int = 19,district_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,lga_name

     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_polling_unit_level.get_polling_lga_all_results(country_name,state_name,district_name,lga_name)



# @app.post("/senateresults_polling/district",tags=["senate Polling Unit results"])
# async def senate_results_polling_country_result(country_name: int = 1,state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_polling_unit_level.get_polling_state_all_results(country_name,state_name,district_name)


# # Ward



# @app.post("/senateresults_ward/lga",tags=["senate Ward results"])
# async def senate_results_ward_lga_result(country_name: int = 1,state_name: int = 19,district_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,state_name,lga_name

     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_ward_level.get_ward_lga_all_results(country_name,state_name,district_name,lga_name)


# @app.post("/senateresults_ward/district",tags=["senate Ward results"])
# async def senate_results_ward_country_result(country_name: int = 1,state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_ward_level.get_ward_country_all_results(country_name,state_name,district_name)



# # Lga



# @app.post("/senateresults_lga/district", tags=["senate LGA results"])
# async def senate_results_lga_country_result(country_name: int = 1,state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):

#     '''

     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_lga_level.get_lga_state_all_results(country_name,state_name,district_name)





# # Country 
# @app.post("/senateresults_district/district", tags=["senate district results"])
# async def senate_results_country_country_result(country_name: int = 1,state_name: int = 19,district_name: int =1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''     
#      Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_results_state_level.get_state_state_all_results(country_name,state_name,district_name)





"""......................................................Results of rep ........................................"""


# Polling page

@app.post("/represults_polling/ward",tags=["rep Polling Unit results"])
async def rep_results_polling_ward_result(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_polling_unit_level.get__polling_ward_all_results(country_name,state_name,constituency_name,lga_name,ward_name)

@app.post("/represults_polling/lga",tags=["rep Polling Unit results"])
async def rep_results_polling_lga_result(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_polling_unit_level.get_polling_lga_all_results(country_name,state_name,constituency_name,lga_name)



@app.post("/represults_polling/constituency",tags=["rep Polling Unit results"])
async def rep_results_polling_country_result(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_polling_unit_level.get_polling_state_all_results(country_name,state_name,constituency_name)


# Ward



@app.post("/represults_ward/lga",tags=["rep Ward results"])
async def rep_results_ward_lga_result(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_ward_level.get_ward_lga_all_results(country_name,state_name,constituency_name,lga_name)


@app.post("/represults_ward/constituency",tags=["rep Ward results"])
async def rep_results_ward_country_result(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_ward_level.get_ward_state_all_results(country_name,state_name,constituency_name)



# Lga




@app.post("/represults_lga/constituency", tags=["rep LGA results"])
async def rep_results_lga_country_result(country_name: int = 1,state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):

    '''

     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_lga_level.get_lga_state_all_results(country_name,state_name,constituency_name)





# Country 
@app.post("/represults_constituency/constituency", tags=["rep constituency results"])
async def rep_results_country_country_result(country_name: int = 1,state_name: int = 19,constituency_name: int =1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''     
     Input request data - party check box data for example {"1":"ADC","2":"NNPP"}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_results_state_level.get_state_state_all_results(country_name,state_name,constituency_name)




"'''''''''''''''''''''''''''''''''''''''''''''''''''''''''ANalysis Presidential''''''''''''''''''''''''''''''"



# Analysis Tab1 presidential


# Polling page
@app.get("/presidentialanalysis_polling_tab1/pu",tags=["Presidential Polling Unit Analysis Tab1"])
async def presidential_results_polling_pu_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name,pu_name


    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level.get__polling_pu_all_results(country_name,state_name, lga_name, ward_name,pu_name)

@app.get("/presidentialanalysis_polling_tab1/ward",tags=["Presidential Polling Unit Analysis Tab1"])
async def presidential_results_polling_ward_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level.get__polling_ward_all_results(country_name,state_name, lga_name,ward_name)

@app.get("/presidentialanalysis_polling_tab1/lga",tags=["Presidential Polling Unit Analysis Tab1"])
async def presidential_results_polling_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level.get_polling_lga_all_results(country_name,state_name,lga_name)

@app.get("/presidentialanalysis_polling_tab1/state",tags=["Presidential Polling Unit Analysis Tab1"])
async def presidential_results_polling_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name
     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_analysis_polling_unit_level.get_polling_state_all_results(country_name,state_name)

# @app.get("/presidentialanalysis_polling_tab1/country",tags=["Presidential Polling Unit Analysis Tab1"])
# async def presidential_results_polling_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#        Input params -  coutry_name
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_analysis_polling_unit_level.get_polling_country_all_results(country_name)


# Ward


@app.get("/presidentialanalysis_ward_tab1/ward", tags=["Presidential Ward Analysis Tab1"])
async def presidential_results_ward_ward_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level.get_ward_ward_all_results(country_name,state_name, lga_name,ward_name)

@app.get("/presidentialanalysis_ward_tab1/lga",tags=["Presidential Ward Analysis Tab1"])
async def presidential_results_ward_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params - coutry_name,state_name,lga_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level.get_ward_lga_all_results(country_name,state_name,lga_name)

@app.get("/presidentialanalysis_ward_tab1/state", tags=["Presidential Ward Analysis Tab1"])
async def presidential_results_ward_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level.get_ward_state_all_results(country_name,state_name)

# @app.get("/presidentialanalysis_ward_tab1/country",tags=["Presidential Ward Analysis Tab1"])
# async def presidential_results_ward_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''    
#     Input params - coutry_name 
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_analysis_ward_level.get_ward_country_all_results(country_name)



# Lga
@app.get("/presidentialanalysis_lga_tab1/lga",tags=["Presidential LGA Analysis Tab1"])
async def presidential_results_lga_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_analysis_lga_level.get_lga_lga_all_results(country_name,state_name,lga_name)


@app.get("/presidentialanalysis_lga_tab1/state", tags=["Presidential LGA Analysis Tab1"])
async def presidential_results_lga_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_lga_level.get_lga_state_all_results(country_name,state_name)

# @app.get("/presidentialanalysis_lga_tab1/country", tags=["Presidential LGA Analysis Tab1"])
# async def presidential_results_lga_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):

#     '''
#     Input params - coutry_name
     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_analysis_lga_level.get_lga_country_all_results(country_name)

# State
@app.get("/presidentialanalysis_state_tab1/state", tags=["Presidential State Analysis Tab1"])
async def presidential_results_state_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_state_level.get_state_state_all_results(country_name,state_name)

# @app.get("/presidentialanalysis_state_tab1/country", tags=["Presidential State Analysis Tab1"])
# async def presidential_results_state_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#     Input params - coutry_name

#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_analysis_state_level.get_state_country_all_results(country_name)

# Country 
# @app.get("/presidentialanalysis_country_tab1/country", tags=["Presidential Country Analysis Tab1"])
# async def presidential_results_country_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     ''' 
#     Input params - coutry_name  
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return presidential_analysis_country_level.get_country_country_all_results(country_name)


'''...............................................................................................................'''


"'''''''''''''''''''''''''''''''''''''''''''''''''''''''''ANalysis senate''''''''''''''''''''''''''''''"



# # Analysis Tab1 senate


# # Polling page
# @app.get("/senateanalysis_polling_tab1/pu",tags=["senate Polling Unit Analysis Tab1"])
# async def senate_results_polling_pu_result(state_name: int = 19,district_name: int = 1,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name,lga_name,ward_name,pu_name


#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_polling_unit_level.get__polling_pu_all_results(state_name,district_name, lga_name, ward_name,pu_name)

# @app.get("/senateanalysis_polling_tab1/ward",tags=["senate Polling Unit Analysis Tab1"])
# async def senate_results_polling_ward_result(state_name: int = 19,district_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name,lga_name,ward_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_polling_unit_level.get__polling_ward_all_results(state_name,district_name, lga_name,ward_name)

# @app.get("/senateanalysis_polling_tab1/lga",tags=["senate Polling Unit Analysis Tab1"])
# async def senate_results_polling_lga_result(state_name: int = 19,district_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name,lga_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_polling_unit_level.get_polling_lga_all_results(state_name,district_name,lga_name)

# @app.get("/senateanalysis_polling_tab1/district",tags=["senate Polling Unit Analysis Tab1"])
# async def senate_results_polling_state_result(state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name
     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
    
#     return senate_analysis_polling_unit_level.get_polling_state_all_results(state_name,district_name)


# # Ward


# @app.get("/senateanalysis_ward_tab1/ward", tags=["senate Ward Analysis Tab1"])
# async def senate_results_ward_ward_result(state_name: int = 19,district_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name,lga_name,ward_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_ward_level.get_ward_ward_all_results(state_name,district_name, lga_name,ward_name)

# @app.get("/senateanalysis_ward_tab1/lga",tags=["senate Ward Analysis Tab1"])
# async def senate_results_ward_lga_result(state_name: int = 19,district_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params - coutry_name,district_name,lga_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_ward_level.get_ward_lga_all_results(state_name,district_name,lga_name)

# @app.get("/senateanalysis_ward_tab1/district", tags=["senate Ward Analysis Tab1"])
# async def senate_results_ward_state_result(state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name

#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_ward_level.get_ward_state_all_results(state_name,district_name)



# # Lga
# @app.get("/senateanalysis_lga_tab1/lga",tags=["senate LGA Analysis Tab1"])
# async def senate_results_lga_lga_result(state_name: int = 19,district_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name,lga_name

#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
    
#     return senate_analysis_lga_level.get_lga_lga_all_results(state_name,district_name,lga_name)


# @app.get("/senateanalysis_lga_tab1/district", tags=["senate LGA Analysis Tab1"])
# async def senate_results_lga_state_result(state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_lga_level.get_lga_state_all_results(state_name,district_name)



# @app.get("/senateanalysis_district_tab1/district", tags=["senate district Analysis Tab1"])
# async def senate_results_lga_state_result(state_name: int = 19,district_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
#     '''
#      Input params -  coutry_name,district_name

     
#     '''
#     if not credentials:
#         raise HTTPException(status_code=401, detail='my-custom-details')
#     return senate_analysis_country_level.get_country_country_all_results(state_name,district_name)






'''...............................................................................................................'''

"'''''''''''''''''''''''''''''''''''''''''''''''''''''''''ANalysis rep''''''''''''''''''''''''''''''"



# Analysis Tab1 rep


# Polling page
@app.get("/repanalysis_polling_tab1/pu",tags=["rep Polling Unit Analysis Tab1"])
async def rep_results_polling_pu_result(state_name: int = 19,constituency_name: int = 1,lga_name: int = 10,ward_name: int = 1,pu_name:int=1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name,lga_name,ward_name,pu_name


    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_polling_unit_level.get__polling_pu_all_results(state_name,constituency_name, lga_name, ward_name,pu_name)

@app.get("/repanalysis_polling_tab1/ward",tags=["rep Polling Unit Analysis Tab1"])
async def rep_results_polling_ward_result(state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name,lga_name,ward_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_polling_unit_level.get__polling_ward_all_results(state_name,constituency_name, lga_name,ward_name)

@app.get("/repanalysis_polling_tab1/lga",tags=["rep Polling Unit Analysis Tab1"])
async def rep_results_polling_lga_result(state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name,lga_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_polling_unit_level.get_polling_lga_all_results(state_name,constituency_name,lga_name)

@app.get("/repanalysis_polling_tab1/constituency",tags=["rep Polling Unit Analysis Tab1"])
async def rep_results_polling_state_result(state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name
     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return rep_analysis_polling_unit_level.get_polling_state_all_results(state_name,constituency_name)


# Ward


@app.get("/repanalysis_ward_tab1/ward", tags=["rep Ward Analysis Tab1"])
async def rep_results_ward_ward_result(state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name,lga_name,ward_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_ward_level.get_ward_ward_all_results(state_name,constituency_name, lga_name,ward_name)

@app.get("/repanalysis_ward_tab1/lga",tags=["rep Ward Analysis Tab1"])
async def rep_results_ward_lga_result(state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params - coutry_name,constituency_name,lga_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_ward_level.get_ward_lga_all_results(state_name,constituency_name,lga_name)

@app.get("/repanalysis_ward_tab1/constituency", tags=["rep Ward Analysis Tab1"])
async def rep_results_ward_state_result(state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_ward_level.get_ward_state_all_results(state_name,constituency_name)



# Lga
@app.get("/repanalysis_lga_tab1/lga",tags=["rep LGA Analysis Tab1"])
async def rep_results_lga_lga_result(state_name: int = 19,constituency_name: int = 1,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name,lga_name

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return rep_analysis_lga_level.get_lga_lga_all_results(state_name,constituency_name,lga_name)


@app.get("/repanalysis_lga_tab1/constituency", tags=["rep LGA Analysis Tab1"])
async def rep_results_lga_state_result(state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_lga_level.get_lga_state_all_results(state_name,constituency_name)





@app.get("/repanalysis_constituency_tab1/constituency", tags=["rep Constituency Analysis Tab1"])
async def rep_results_lga_state_result(state_name: int = 19,constituency_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,constituency_name
     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return rep_analysis_country_level.get_country_country_all_results(state_name,constituency_name)



'''...............................................................................................................'''















# Anaalysis Tab2 presidential


# Polling page
@app.post("/presidentialanalysis_polling_tab2/pu",tags=["Presidential Polling Unit Analysis Tab2"])
async def presidential_results_polling_pu_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,pu_name:int=1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name,pu_name

    Input params  -  party name example {"party_name":"NNPP",level:""}
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level_party.get__polling_pu_all_results(country_name,state_name, lga_name, ward_name,pu_name,data)

@app.post("/presidentialanalysis_polling_tab2/ward",tags=["Presidential Polling Unit Analysis Tab2"])
async def presidential_results_polling_ward_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name
    
    Input params  -  party name example {"party_name":"NNPP","level":""}

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level_party.get__polling_ward_all_results(country_name,state_name, lga_name,ward_name,data)

@app.post("/presidentialanalysis_polling_tab2/lga",tags=["Presidential Polling Unit Analysis Tab2"])
async def presidential_results_polling_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name
        
    Input params  -  party name and level example {"party_name":"NNPP","level":"pu or ward"}

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level_party.get_polling_lga_all_results(country_name,state_name,lga_name,data)

@app.post("/presidentialanalysis_polling_tab2/state",tags=["Presidential Polling Unit Analysis Tab2"])
async def presidential_results_polling_state_result(country_name: int = 1,state_name: int = 19,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name
     
    Input params  -  party name example {"party_name":"NNPP","level":"pu or ward or lga"}

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_analysis_polling_unit_level_party.get_polling_state_all_results(country_name,state_name,data)

@app.post("/presidentialanalysis_polling_tab2/country",tags=["Presidential Polling Unit Analysis Tab2"])
async def presidential_results_polling_country_result(country_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
       Input params -  coutry_name


        Input params  -  party name example {"party_name":"NNPP","level":"pu or ward or lga or state"}


    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level_party.get_polling_country_all_results(country_name,data)


# Ward


@app.post("/presidentialanalysis_ward_tab2/ward", tags=["Presidential Ward Analysis Tab2"])
async def presidential_results_ward_ward_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name,ward_name

    Input params  -  party name example {"party_name":"NNPP",level:""}


    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    print(data)
    return presidential_analysis_ward_level_party.get_ward_ward_all_results(country_name,state_name, lga_name,ward_name,data)

@app.post("/presidentialanalysis_ward_tab2/lga",tags=["Presidential Ward Analysis Tab2"])
async def presidential_results_ward_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params - coutry_name,state_name,lga_name
    Input params  -  party name example {"party_name":"NNPP",level:""}

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level_party.get_ward_lga_all_results(country_name,state_name,lga_name,data)

@app.post("/presidentialanalysis_ward_tab2/state", tags=["Presidential Ward Analysis Tab2"])
async def presidential_results_ward_state_result(country_name: int = 1,state_name: int = 19,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name
         Input params  -  party name example {"party_name":"NNPP",level:"lga" or "ward"}


    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level_party.get_ward_state_all_results(country_name,state_name,data)

@app.post("/presidentialanalysis_ward_tab2/country",tags=["Presidential Ward Analysis Tab2"])
async def presidential_results_ward_country_result(country_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''    
    Input params - coutry_name 
        Input params  -  party name example {"party_name":"NNPP",level:"lga" or "ward" or "state"}

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level_party.get_ward_country_all_results(country_name,data)



# Lga
@app.post("/presidentialanalysis_lga_tab2/lga",tags=["Presidential LGA Analysis Tab2"])
async def presidential_results_lga_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name,lga_name

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_analysis_lga_level_party.get_lga_lga_all_results(country_name,state_name,lga_name,data)


@app.post("/presidentialanalysis_lga_tab2/state", tags=["Presidential LGA Analysis Tab2"])
async def presidential_results_lga_state_result(country_name: int = 1,state_name: int = 19,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_lga_level_party.get_lga_state_all_results(country_name,state_name,data)

@app.post("/presidentialanalysis_lga_tab2/country", tags=["Presidential LGA Analysis Tab2"])
async def presidential_results_lga_country_result(country_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):

    '''
    Input params - coutry_name
     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_lga_level_party.get_lga_country_all_results(country_name,data)

# State
@app.post("/presidentialanalysis_state_tab2/state", tags=["Presidential State Analysis Tab2"])
async def presidential_results_state_state_result(country_name: int = 1,state_name: int = 19,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
     Input params -  coutry_name,state_name

     
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_state_level_party.get_state_state_all_results(country_name,state_name,data)

@app.post("/presidentialanalysis_state_tab2/country", tags=["Presidential State Analysis Tab2"])
async def presidential_results_state_country_result(country_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    '''
    Input params - coutry_name

    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_state_level_party.get_state_country_all_results(country_name,data)

# Country 
@app.post("/presidentialanalysis_country_tab2/country", tags=["Presidential Country Analysis Tab2"])
async def presidential_results_country_country_result(country_name: int = 1,data:dict=Body(...),credentials: HTTPAuthorizationCredentials = Security(security)):
    ''' 
    Input params - coutry_name  
    '''
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_country_level_party.get_country_country_all_results(country_name,data)
'''...............................................................................................................'''





















"''''''''''''''''''''''''''Analysis Tab3 '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
# Polling page
@app.get("/presidentialanalysis_polling_tab3/pu",tags=["Presidential Polling Unit Analysis Tab3"])
async def presidential_results_polling_pu_result(credentials: HTTPAuthorizationCredentials = Security(security)):
  
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_polling_unit_level_prediction.get__polling_pu_all_results()

@app.get("/presidentialanalysis_polling_tab3/ward",tags=["Presidential Polling Unit Analysis Tab3"])
async def presidential_results_polling_ward_result(credentials: HTTPAuthorizationCredentials = Security(security)):
  
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level_prediction.get_ward_ward_all_results()

@app.get("/presidentialanalysis_polling_tab3/lga",tags=["Presidential Polling Unit Analysis Tab3"])
async def presidential_results_polling_lga_result(credentials: HTTPAuthorizationCredentials = Security(security)):

    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_lga_level_prediction.get_lga_lga_all_results()

@app.get("/presidentialanalysis_polling_tab3/state",tags=["Presidential Polling Unit Analysis Tab3"])
async def presidential_results_polling_state_result(credentials: HTTPAuthorizationCredentials = Security(security)):
  
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_analysis_state_level_prediction.get_state_state_all_results()

@app.get("/presidentialanalysis_polling_tab3/country",tags=["Presidential Polling Unit Analysis Tab3"])
async def presidential_results_polling_country_result(credentials: HTTPAuthorizationCredentials = Security(security)):
   
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_country_level_prediction.get_country_country_all_results()




@app.get("/presidentialanalysis_polling_comparism/ward",tags=["Presidential Comparism"])
async def presidential_results_polling_ward_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,ward_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
  
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_ward_level_comparism.get_ward_ward_all_results(country_name,state_name,lga_name,ward_name)

@app.get("/presidentialanalysis_polling_comparism/lga",tags=["Presidential Comparism"])
async def presidential_results_polling_lga_result(country_name: int = 1,state_name: int = 19,lga_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):

    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_lga_level_comparism.get_lga_lga_all_results(country_name,state_name,lga_name)

@app.get("/presidentialanalysis_polling_comparism/state",tags=["Presidential Comparism"])
async def presidential_results_polling_state_result(country_name: int = 1,state_name: int = 19,credentials: HTTPAuthorizationCredentials = Security(security)):
  
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    
    return presidential_analysis_state_level_comparism.get_state_state_all_results(country_name,state_name)

@app.get("/presidentialanalysis_polling_comparism/country",tags=["Presidential Comparism"])
async def presidential_results_polling_country_result(country_name: int = 1,credentials: HTTPAuthorizationCredentials = Security(security)):
   
    if not credentials:
        raise HTTPException(status_code=401, detail='my-custom-details')
    return presidential_analysis_country_level_comparism.get_country_country_all_results(country_name)
































'''....................................................Mobile app routes.................................................... '''





#  routes for mobile application
@app.post("/mobile_submit",  tags=["Mobile app routes"])
async def check_number_collate(user:dict= Body(...),userdata_collate:dict= Body(...)):
    
    """
      This route is for collation submit
    """


    return mobile.submit_data(user,userdata_collate)

#  routes for mobile application
@app.post("/mobile_submit-senate",  tags=["Mobile app routes"])
async def check_number_collate(user:dict= Body(...),userdata_collate:dict= Body(...)):
    
    """
      This route is for collation submit
    """


    return mobile.submit_data_senate(user,userdata_collate)

#  routes for mobile application
@app.post("/mobile_submit-rep",  tags=["Mobile app routes"])
async def check_number_collate(user:dict= Body(...),userdata_collate:dict= Body(...)):
    
    """
      This route is for collation submit
    """


    return mobile.submit_data_rep(user,userdata_collate)



@app.post("/mobile-cancel",tags=["Mobile app routes"])
async def check_number_cancel(user:dict= Body(...),userdata_collate:dict= Body(...)):
    """
      This route is for collation cancel
    """

    
    return mobile.cancel_data(user,userdata_collate)


@app.post("/mobile-cancel-senate",tags=["Mobile app routes"])
async def check_number_cancel(user:dict= Body(...),userdata_collate:dict= Body(...)):
    """
      This route is for collation cancel
    """

    
    return mobile.cancel_data_senate(user,userdata_collate)

@app.post("/mobile-cancel-rep",tags=["Mobile app routes"])
async def check_number_cancel(user:dict= Body(...),userdata_collate:dict= Body(...)):
    """
      This route is for collation cancel
"""
    
    return mobile.cancel_data_rep(user,userdata_collate)

@app.post("/mobile-postmedia",tags=["Mobile app routes"])
async def check_number_postmedia(user:dict= Body(...),userdata_collate:dict= Body(...)):
    """
      This route is for post images or videos

        post - {

            remark : this is from additional remarks 
            file : this is file name
            type : type of the file
            lat : latitude
            long : longitude
            phone : take this value from check-number response
            email : take this value from check-number response

        }

    """
   
    return mobile.upload_data(user,userdata_collate)


@app.post("/mobile-message",tags=["Mobile app routes"])
async def check_number_message(user:dict= Body(...)):
    """
      This route is for message

      input -  user data from login repsonse

    """
    return mobile.message(user)

@app.post("/mobile-getdata",tags=["Mobile app routes"])
async def check_number_message(user:dict= Body(...)):
    """
      This route to get current data of collation form

      input -  user data from login repsonse

    """
    return mobile.get_data(user)


@app.post("/mobile-getdata-senate",tags=["Mobile app routes"])
async def check_number_message(user:dict= Body(...)):
    """
      This route to get current data of collation form

      input -  user data from login repsonse

    """
    return mobile.get_data_senate(user)

@app.post("/mobile-getdata-rep",tags=["Mobile app routes"])
async def check_number_message(user:dict= Body(...)):
    """
      This route to get current data of collation form

      input -  user data from login repsonse

    """
    return mobile.get_data_rep(user)



@app.post("/aiprediction",tags=["Mobile app routes"])
async def check_number_message(user:dict= Body(...), image:str=None):
    """

      input -  user data from login repsonse
      input2 - image url

    """
    return upload_data.ai(user,image)

@app.get('/mlPredict',tags=["Mobile app routes"])
def mlprediction(urlkey: str= None,credentials: HTTPAuthorizationCredentials = Security(security)):
    url = "https://api.clip.jina.ai:8443/post"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] ="5410503a33dee287bf3bb7a5f6b9653c"
    data = f"""{{"data":[{{"uri": "{urlkey}",
    "matches": [{{"text": "people walking on a street"}},
            {{"text": "fight on a street"}},
            {{"text": "fire on a street"}},
            {{"text": "Result Document"}},
            {{"text": "People sitting in the office"}},
            {{"text": "People voting near ballot box"}},
            {{"text": "street violence"}},
            {{"text": "car crash"}},
            {{"text": "cars on a road"}},
            {{"text": "violence in office"}},
            {{"text": "person walking in office"}},
            {{"text": "Gun in the street"}},
            {{"text": "People fighting with Guns"}},
            {{"text": "Bandits on bike with Weapon"}},
            {{"text": "Explosive device"}},
            {{"text": "Knife in a hand"}}
            ]}}],
            "execEndpoint":"/rank"}}
    """
    resp = requests.post(url, headers=headers, data=data)
    resp = resp.json()
    # return {"dummy":"0"}
    v = resp['data'][0]['matches']
    outputlabel = v[0]['text']
    outputscore = v[0]['scores']['clip_score']['value']
    results = {outputlabel: outputscore}
    return results


""".....................Dashboard.................... """

from application.app_v1.dashboard import dashboard
@app.post("/dashboard_pollingunit",tags=["Dashboard routes"])
async def dashboardpu(type:str= Body(...),constiuency_name:int= Body(...)):

 
    return dashboard.pollingunit_dashboard(type,constiuency_name)



@app.post("/dashboard_ward",tags=["Dashboard routes"])
async def dashboardpu(type:str= Body(...),constiuency_name:int= Body(...)):

 
    return dashboard.ward_dashboard(type,constiuency_name)



@app.post("/dashboard_lga",tags=["Dashboard routes"])
async def dashboardpu(type:str= Body(...),constiuency_name:int= Body(...)):

 
    return dashboard.lga_dashboard(type,constiuency_name)



# @app.post("/dashboard_district",tags=["Dashboard routes"])
# async def dashboardpu():

 
#     return dashboard.district_dashboard()

@app.post("/dashboard_rep",tags=["Dashboard routes"])
async def dashboardpu(constiuency_name:int= Body(...)):

 
    return dashboard.constituency_dashboard(constiuency_name)


@app.post("/dashboard_state",tags=["Dashboard routes"])
async def dashboardpu():

 
    return dashboard.state_dashboard()

import json
@app.post("/usermanagement_place",tags=["Dashboard routes"])
async def dashboardpu(user:dict= Body(...)):
    # user = json.dumps(user)
    return dashboard.place(user)



# from PIL import Image
# import io
# # Take in base64 string and return cv image
# def stringToRGB(base64_string):
#     imgdata = base64.b64decode(str(base64_string))
#     img = Image.open(io.BytesIO(imgdata))
#     opencv_img= cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
#     return opencv_img 

#  routes for mobile application
# import math,io
# def JPEGSaveWithTargetSize(im, filename, target):
#    """Save the image as JPEG with the given name at best quality that makes less than "target" bytes"""
#    # Min and Max quality
#    Qmin, Qmax = 25, 96
#    # Highest acceptable quality found
#    Qacc = -1
#    while Qmin <= Qmax:
#       m = math.floor((Qmin + Qmax) / 2)

#       # Encode into memory and get size
#       buffer = io.BytesIO()
#       im.save(buffer, format="JPEG", quality=m)
#       s = buffer.getbuffer().nbytes

#       if s <= target:
#          Qacc = m
#          Qmin = m + 1
#       elif s > target:
#          Qmax = m - 1

#    # Write to disk at the defined quality
#    if Qacc > -1:
#       im.save(filename, format="JPEG", quality=Qacc)
#    else:
#       print("ERROR: No acceptble quality factor found", file=sys.stderr)

# import boto3
# import base64
# import numpy as np
# import cv2
# try:
#     from skimage import filters
# except ImportError:
#     from skimage import filter as filters
# from parser2 import *
# from pdf2image import convert_from_path
# import urllib.request
# import shutil
# @app.post("/mobile-scanner",  tags=["Mobile app routes"])
# async def check_nr_collate(pucode:str=None,imageurl:str=None):
#     try:
        
#         textract = boto3.client("textract")
#         # encoded_img = user['image'].split(",")[1]
#         # binary = base64.b64decode(encoded_img)
#         # image = np.asarray(bytearray(binary), dtype=np.uint8)
#         # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#         # print(img_np_arr)
#         file_name = 'filename.pdf'

#         response = requests.get(imageurl, stream=True)
#         try:
#             with open(file_name, 'wb') as fd:
#                 for chunk in response .iter_content(chunk_size=128):
#                     fd.write(chunk)

#         except:
#             pass

#         # urllib.request.urlretrieve(imageurl, "filename.pdf")
#         images = convert_from_path('filename.pdf')
#         images.save('result.jpg', optimize=True, quality=95)  # The saved downsized image size is 22.9kb

#         print("imgae",images)

#         # JPEGSaveWithTargetSize(images, "result.jpg", 4000000)
#         print("imgae",images)
#         # pil_image_lst = convert_from_path('filename.pdf')
#         # print(pil_image)
#         # pil_image = pil_image_lst[0]
#         # image = np.array(images) 
#         # print(image)
#         # img_object = cv2.imdecode(img_np_arr, cv2.IMREAD_COLOR)
#         image = cv2.imread('result.jpg')
#         print("cv",image)
#         gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#         # blur
#         smooth = cv2.GaussianBlur(gray, (33,33), 0)

#         division = cv2.divide(gray, smooth, scale=255)

# # sharpen using unsharp masking
#         sharp = filters.unsharp_mask(division, radius=1.5, amount=2.5, multichannel=False, preserve_range=False)
#         sharp = (255*sharp).clip(0,255).astype(np.uint8)
       
#         is_success, im_buf_arr = cv2.imencode(".jpg", sharp)
#         byte_im = im_buf_arr.tobytes()
#         print('ok')

#         response = textract.analyze_document(Document={'Bytes': byte_im}, FeatureTypes=["FORMS", "TABLES"])
#         raw_text = extract_text(response, extract_by="LINE")
#         word_map = map_word_id(response)
#         table = extract_table_info(response, word_map)
#         key_map = get_key_map(response, word_map)
#         value_map = get_value_map(response, word_map)
#         final_map = get_kv_map(key_map, value_map)
#         for key,value in table.items():
#             table = value
#     except Exception:
#         return {"message": "There was an error uploading the file"}
 
        
#     return mobile.scanner(pucode,raw_text,table,final_map,sharp)

















handler = Mangum(app=app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",  reload=True, access_log=False,port=8000)
