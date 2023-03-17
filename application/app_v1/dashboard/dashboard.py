from application.app_v1.database import get_db
from datetime import datetime
from datetime import datetime
import json
from application.app_v1.dashboard.party_table import presidential_table_pu,presidential_table_pu_rep,presidential_table_ward,presidential_table_lga,presidential_table_state,presidential_table_const_rep,presidential_table_lga_rep,presidential_table_ward_rep


conditions_pu = {
     
            "Registered Voters":f"""{presidential_table_pu['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  pu_result_table""",
            "Accredited Voters":f"""{presidential_table_pu['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  pu_result_table""",
            "Valid Voters":f"""{presidential_table_pu['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  pu """,
            "slider_gragh":f"""{presidential_table_pu['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_pu['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=11212, 'collation completed','collation in progress......')) as message 
 		from pu_result_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_pu['query']}  select count(*) as count1 from pu_result_table where (status='collated' or status='canceled') """,
            "total_pu":f"""{presidential_table_pu['query']} select count(*) AS count1 from pu_result_table""" ,
            "collated":f"""{presidential_table_pu['query']} select count(*) as count1 from pu_result_table where status='collated'""",
            "collated_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='collated'""",
            "non-collated":f"""{presidential_table_pu['query']} select count(*) as count1 from pu_result_table where status='non collated'""",
            "non-collated_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='non collated'""",
            "cancelled":f"""{presidential_table_pu['query']} select count(*) as count1 from pu where status='canceled'""",
            "cancelled_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='canceled'""",
            "over-voting":f"""{presidential_table_pu['query']} select count(*) as count1 from pu where over_vote_values>0 """,
            "over-voting_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code,pu_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from pu where over_vote_values>0""",
            "scores": f"""{presidential_table_pu['query']} select NNPP,APC,PDP,ADP from st """,
            
            # "PU_won_NNPP":f"""{presidential_table_pu['query']}  select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" """,
           
           
            # "PU_won_NNPP_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
# WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" """,


            "Wards_led_NNPP":f"""{presidential_table_pu['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"          """,
            "Wards_led_NNPP_table":f"""{presidential_table_pu['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  """,
            "Lga's_led_NNPP":f"""{presidential_table_pu['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"       """,
            "Lga's_led_NNPP_table":f"""{presidential_table_pu['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"     """,
            # "PU_won_APC":f"""{presidential_table_pu['query']}  select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="APC" """,
            # "PU_won_APC_table": f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
# WHERE row_num<2 and total_valid_votes>0  AND party="APC" """,
            "Wards_led_APC":f"""{presidential_table_pu['query']}   select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="APC"       """,
            "Wards_led_APC_table":f"""{presidential_table_pu['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"    """,
            "Lga's_led_APC":f"""{presidential_table_pu['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"          """,
            "Lga's_led_APC_table":f"""{presidential_table_pu['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"     """,
            #  "PU_won_PDP":f"""{presidential_table_pu['query']} select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="PDP" """,
            # "PU_won_PDP_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
# WHERE row_num<2 and total_valid_votes>0  AND party="PDP" """,
            "Wards_led_PDP":f"""{presidential_table_pu['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  """,
            "Wards_led_PDP_table":f"""{presidential_table_pu['query']}    select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"      """,
            "Lga's_led_PDP":f"""{presidential_table_pu['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"           """,
            "Lga's_led_PDP_table":f"""{presidential_table_pu['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"         """,
            # "PU_won_ADP":f"""{presidential_table_pu['query']}   select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="ADP"
#  """,
            # "PU_won_ADP_table":f"""{presidential_table_pu['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
# WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Wards_led_ADP":f"""{presidential_table_pu['query']}       select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="ADP"             """,
            "Wards_led_ADP_table":f"""{presidential_table_pu['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP"    """,
            "Lga's_led_ADP":f"""{presidential_table_pu['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"                   """,
            "Lga's_led_ADP_table":f"""{presidential_table_pu['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Party Led in Kano State":f"""{presidential_table_pu['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1
         """
            

    }
conditions_ward = {
     
            "Registered Voters":f"""{presidential_table_ward['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  ward_result_table""",
            "Accredited Voters":f"""{presidential_table_ward['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  ward_result_table""",
            "Valid Voters":f"""{presidential_table_ward['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  wt """,
            "slider_gragh":f"""{presidential_table_ward['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_ward['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=484, 'collation completed','collation in progress......')) as message 
 		from ward_result_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_ward['query']}  select count(*) as count1 from ward_result_table where (status='collated' or status='canceled') """,
            "total_ward":f"""{presidential_table_ward['query']} select count(*) AS count1 from ward_result_table""" ,
            "collated":f"""{presidential_table_ward['query']} select count(*) as count1 from ward_result_table where status='collated'""",
            "collated_table":f"""{presidential_table_ward['query']} select lga_name,ward_name,remarks from wt where status='collated'""",
            "non-collated":f"""{presidential_table_ward['query']} select count(*) as count1 from ward_result_table where status='non collated'""",
            "non-collated_table":f"""{presidential_table_ward['query']} select lga_name,ward_name,remarks from wt where status='non collated'""",
            "cancelled":f"""{presidential_table_ward['query']} select count(*) as count1 from wt where status='canceled'""",
            "cancelled_table":f"""{presidential_table_ward['query']} select lga_name,ward_name,remarks from wt where status='canceled'""",
            "over-voting":f"""{presidential_table_ward['query']} select count(*) as count1 from wt where over_vote_values>0 """,
            "over-voting_table":f"""{presidential_table_ward['query']} select lga_name,ward_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from wt where over_vote_values>0""",
            "scores": f"""{presidential_table_ward['query']} select NNPP,APC,PDP,ADP from st """,
  

            "Wards_led_NNPP":f"""{presidential_table_ward['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"          """,
            "Wards_led_NNPP_table":f"""{presidential_table_ward['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  """,
            "Lga's_led_NNPP":f"""{presidential_table_ward['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"       """,
            "Lga's_led_NNPP_table":f"""{presidential_table_ward['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"     """,
            
   
            
            "Wards_led_APC":f"""{presidential_table_ward['query']}   select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="APC"       """,
            "Wards_led_APC_table":f"""{presidential_table_ward['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"    """,
            "Lga's_led_APC":f"""{presidential_table_ward['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"          """,
            "Lga's_led_APC_table":f"""{presidential_table_ward['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"     """,

            
            "Wards_led_PDP":f"""{presidential_table_ward['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  """,
            "Wards_led_PDP_table":f"""{presidential_table_ward['query']}    select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"      """,
            "Lga's_led_PDP":f"""{presidential_table_ward['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"           """,
            "Lga's_led_PDP_table":f"""{presidential_table_ward['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"         """,
            

            "Wards_led_ADP":f"""{presidential_table_ward['query']}       select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="ADP"             """,
            "Wards_led_ADP_table":f"""{presidential_table_ward['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP"    """,
            "Lga's_led_ADP":f"""{presidential_table_ward['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"                   """,
            "Lga's_led_ADP_table":f"""{presidential_table_ward['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Party Led in Kano State":f"""{presidential_table_ward['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1
         """
            

    }

conditions_lga = {
     
            "Registered Voters":f"""{presidential_table_lga['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  lga_result_table""",
            "Accredited Voters":f"""{presidential_table_lga['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  lga_result_table""",
            "Valid Voters":f"""{presidential_table_lga['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  lgat """,
            "slider_gragh":f"""{presidential_table_lga['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_lga['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=774, 'collation completed','collation in progress......')) as message 
 		from lga_result_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_lga['query']}  select count(*) as count1 from lga_result_table where (status='collated' or status='canceled') """,
            "total_lga":f"""{presidential_table_lga['query']} select count(*) AS count1 from lga_result_table""" ,
            "collated":f"""{presidential_table_lga['query']} select count(*) as count1 from lga_result_table where status='collated'""",
            "collated_table":f"""{presidential_table_lga['query']} select lga_name,remarks from lgat where status='collated'""",
            "non-collated":f"""{presidential_table_lga['query']} select count(*) as count1 from lga_result_table where status='non collated'""",
            "non-collated_table":f"""{presidential_table_lga['query']} select lga_name,remarks from lgat where status='non collated'""",
            "cancelled":f"""{presidential_table_lga['query']} select count(*) as count1 from lgat where status='canceled'""",
            "cancelled_table":f"""{presidential_table_lga['query']} select lga_name,remarks from lgat where status='canceled'""",
            "over-voting":f"""{presidential_table_lga['query']} select count(*) as count1 from lgat where over_vote_values>0 """,
            "over-voting_table":f"""{presidential_table_lga['query']} select lga_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from lgat where over_vote_values>0""",
            "scores": f"""{presidential_table_lga['query']} select NNPP,APC,PDP,ADP from st """,
  

 
            "Lga's_led_NNPP":f"""{presidential_table_lga['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"       """,
            "Lga's_led_NNPP_table":f"""{presidential_table_lga['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"     """,
            
   

            
            "Lga's_led_APC":f"""{presidential_table_lga['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"          """,
            "Lga's_led_APC_table":f"""{presidential_table_lga['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"     """,

            

            
            "Lga's_led_PDP":f"""{presidential_table_lga['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"           """,
            "Lga's_led_PDP_table":f"""{presidential_table_lga['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"         """,
            

           
            "Lga's_led_ADP":f"""{presidential_table_lga['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"                   """,
            "Lga's_led_ADP_table":f"""{presidential_table_lga['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Party Led in Kano State":f"""{presidential_table_lga['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1
         """
            

    }

conditions_state = {
     
            "Registered Voters":f"""{presidential_table_state['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  state_result_table""",
            "Accredited Voters":f"""{presidential_table_state['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  state_result_table""",
            "Valid Voters":f"""{presidential_table_state['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  lgat """,
            "slider_gragh":f"""{presidential_table_state['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_state['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=1, 'collation completed','collation in progress......'))  as message 
 		from state_result_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_state['query']}  select count(*) as count1 from state_result_table where (status='collated' or status='canceled') """
         
            

    }







def pollingunit_dashboard(type,constiuency_name):
        conditions_pu_rep = {
     
            "Registered Voters":f"""{presidential_table_pu_rep['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  house_pu_table where house_id={constiuency_name}""",
            "Accredited Voters":f"""{presidential_table_pu_rep['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  house_pu_table where house_id={constiuency_name}""",
            "Valid Voters":f"""{presidential_table_pu_rep['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  pu where state_id=19 and house_id={constiuency_name}""",
            "slider_gragh":f"""{presidential_table_pu_rep['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
            APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
            PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
            ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
            (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
            IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM house where house_id={constiuency_name}		
            """ ,
                        "collation_slider_message":f"""{presidential_table_pu_rep['query']}  select if (count(*)=0 ,'collation not started', 
 		if (count(*)=(select count(*) from house_pu_table where house_id={constiuency_name}), 'collation completed','collation in progress......')) as message
 		from house_pu_table where (status='collated' or status='canceled') and house_id={constiuency_name};			
                """,
                    "collation_slider_value":f"""{presidential_table_pu_rep['query']}   select count(*) from house_pu_table where (status='collated' or status='canceled') and house_id=486 
 (slider range from 0 to 'select count(*) from house_pu_table where house_id={constiuency_name}') """,
                    "total_pu":f"""{presidential_table_pu_rep['query']} select count(*) AS count1 from house_pu_table where house_id={constiuency_name} """ ,
                    "collated":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from house_pu_table where status='collated' and house_id={constiuency_name}""",
                    "collated_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='collated' and house_id={constiuency_name} """,
                    "non-collated":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from house_pu_table where status='non collated' and house_id={constiuency_name} """,
                    "non-collated_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='non collated' and house_id={constiuency_name} """,
                    "cancelled":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from pu where status='canceled' and house_id={constiuency_name} """,
                    "cancelled_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='canceled' and house_id={constiuency_name} """,
                    "over-voting":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from pu where over_vote_values>0 and house_id={constiuency_name} """,
                    "over-voting_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from pu where over_vote_values>0 and house_id={constiuency_name} """,
                    "scores": f"""{presidential_table_pu_rep['query']} select NNPP,APC,PDP,ADP from house where house_id={constiuency_name} """,
                    
                    # "PU_won_NNPP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" and house_id={constiuency_name} """,
                
                
                    # "PU_won_NNPP_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
        # WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" and house_id={constiuency_name}""",


                    "Wards_led_NNPP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  and house_id={constiuency_name}       """,
                    "Wards_led_NNPP_table":f"""{presidential_table_pu_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
        WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  and house_id={constiuency_name} """,
                    "Lga's_led_NNPP":f"""{presidential_table_pu_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  and house_id={constiuency_name}    """,
                    "Lga's_led_NNPP_table":f"""{presidential_table_pu_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
        WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" and house_id={constiuency_name}    """,
                    # "PU_won_APC":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="APC" and house_id={constiuency_name} """,
                    # "PU_won_APC_table": f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
        # WHERE row_num<2 and total_valid_votes>0  AND party="APC"  and house_id={constiuency_name} """,
                    "Wards_led_APC":f"""{presidential_table_pu_rep['query']}   select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="APC" and house_id={constiuency_name}      """,
                    "Wards_led_APC_table":f"""{presidential_table_pu_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
        WHERE row_num<2 and total_valid_votes>0  AND party="APC" and house_id={constiuency_name}   """,
                    "Lga's_led_APC":f"""{presidential_table_pu_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"  and house_id={constiuency_name}        """,
                    "Lga's_led_APC_table":f"""{presidential_table_pu_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
        WHERE row_num<2 and total_valid_votes>0  AND party="APC"  and house_id={constiuency_name}   """,
                    # "PU_won_PDP":f"""{presidential_table_pu_rep['query']} select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="PDP" and house_id={constiuency_name} """,
                    # "PU_won_PDP_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
        # WHERE row_num<2 and total_valid_votes>0  AND party="PDP" and house_id={constiuency_name} """,
                    "Wards_led_PDP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="PDP" and house_id={constiuency_name}  """,
                    "Wards_led_PDP_table":f"""{presidential_table_pu_rep['query']}    select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
        WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  and house_id={constiuency_name}    """,
                    "Lga's_led_PDP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP" and house_id={constiuency_name}        """,
                    "Lga's_led_PDP_table":f"""{presidential_table_pu_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
        WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  and house_id={constiuency_name}       """,
                    # "PU_won_ADP":f"""{presidential_table_pu_rep['query']}   select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="ADP" and house_id={constiuency_name}
        # """,
                    # "PU_won_ADP_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
        # WHERE row_num<2 and total_valid_votes>0  AND party="ADP" and house_id={constiuency_name} """,
                    "Wards_led_ADP":f"""{presidential_table_pu_rep['query']}       select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="ADP"  and house_id={constiuency_name}           """,
                    "Wards_led_ADP_table":f"""{presidential_table_pu_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
        WHERE row_num<2 and total_valid_votes>0  AND party="ADP"   and house_id={constiuency_name} """,
                    "Lga's_led_ADP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"     and house_id={constiuency_name}              """,
                    "Lga's_led_ADP_table":f"""{presidential_table_pu_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
        WHERE row_num<2 and total_valid_votes>0  AND party="ADP" and house_id={constiuency_name} """,
                    "Party Led in Kano State":f"""{presidential_table_pu_rep['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_house  where row_num=1 and house_id={constiuency_name}
                """
                    

            }
        with get_db() as conn:
                cur = conn.cursor()
                key_values = []
                execute_queries = []

   





                if type =='gubernatorial':

                
                        for key,value in conditions_pu.items():
                            execute_queries.append(value)
                            key_values.append(key)
                        ress = {}
                        for index,sql in enumerate(execute_queries):
                                try:
                                    cur.execute(sql)
                                    results = cur.fetchall()
                                    ress[key_values[index]] = results
                                    
                                except:
                                    print('Skipped a sceanrio')

                        ress['table1'] ={"Total Polling Units":{},"collated":{},"non-collated":{},"cancelled":{},"over-voting":{}}
                        ress['table1']['collated']['value'] = ress['collated'][0]['count1']
                        del ress['collated'][0]['count1']
                        ress['table1']['collated']['table'] = ress['collated_table']
                        del ress['collated_table']
                        ress['table1']['non-collated']['value'] = ress['non-collated'][0]['count1']
                        del ress['non-collated'][0]['count1']
                        ress['table1']['non-collated']['table'] = ress['non-collated_table']
                        del ress['non-collated']
                        ress['table1']['cancelled']['value'] = ress['cancelled'][0]['count1']
                        del ress['cancelled'][0]['count1']
                        ress['table1']['cancelled']['table'] = ress['cancelled_table']
                        del ress['cancelled_table']
                        ress['table1']['over-voting']['value'] = ress['over-voting'][0]['count1']
                        del ress['over-voting'][0]['count1']
                        ress['table1']['over-voting']['table'] = ress['over-voting_table']
                        ress['table1']['Total Polling Units']['value'] = ress['total_pu']

                        del ress['over-voting'],ress['total_pu'],ress['collated'],ress['cancelled'],ress['over-voting_table']
                        ress['table2'] ={}

                        ress['table2']['NNPP'] ={"score":ress['scores'][0]['NNPP'],"ward_led":ress['Wards_led_NNPP'],"ward_led_table":ress['Wards_led_NNPP_table'],"lga_led":ress["Lga's_led_NNPP"],"lga_led_table":ress["Lga's_led_NNPP_table"]}
                        ress['table2']['APC'] ={"score":ress['scores'][0]['APC'],"ward_led":ress['Wards_led_APC'],"ward_led_table":ress['Wards_led_APC_table'],"lga_led":ress["Lga's_led_APC"],"lga_led_table":ress["Lga's_led_APC_table"]}
                        ress['table2']['PDP'] ={"score":ress['scores'][0]['PDP'],"ward_led":ress['Wards_led_PDP'],"ward_led_table":ress['Wards_led_PDP_table'],"lga_led":ress["Lga's_led_PDP"],"lga_led_table":ress["Lga's_led_PDP_table"]}
                        ress['table2']['ADP'] ={"score":ress['scores'][0]['ADP'],"ward_led":ress['Wards_led_ADP'],"ward_led_table":ress['Wards_led_ADP_table'],"lga_led":ress["Lga's_led_ADP"],"lga_led_table":ress["Lga's_led_ADP_table"]}
                        del ress['scores'],ress['Wards_led_NNPP'],ress['Wards_led_NNPP_table'],ress["Lga's_led_NNPP"],ress["Lga's_led_NNPP_table"]
                        del ress['Wards_led_APC'],ress['Wards_led_APC_table'],ress["Lga's_led_APC"],ress["Lga's_led_APC_table"]
                        del ress['Wards_led_PDP'],ress['Wards_led_PDP_table'],ress["Lga's_led_PDP"],ress["Lga's_led_PDP_table"]
                        del ress['Wards_led_ADP'],ress['Wards_led_ADP_table'],ress["Lga's_led_ADP"],ress["Lga's_led_ADP_table"]

                        return ress
                        
                                  
                
                    
                elif type =='house-of-assembly':
                    for key,value in conditions_pu_rep.items():
                            execute_queries.append(value)
                            key_values.append(key)
                    ress = {}
                    for index,sql in enumerate(execute_queries):
                            try:
                                cur.execute(sql)
                                results = cur.fetchall()
                                ress[key_values[index]] = results
                                
                            except:
                                print('Skipped a sceanrio')
                    ress['table1'] ={"Total Polling Units":{},"collated":{},"non-collated":{},"cancelled":{},"over-voting":{}}
                    ress['table1']['collated']['value'] = ress['collated'][0]['count1']
                    del ress['collated'][0]['count1']
                    ress['table1']['collated']['table'] = ress['collated_table']
                    del ress['collated_table']
                    ress['table1']['non-collated']['value'] = ress['non-collated'][0]['count1']
                    del ress['non-collated'][0]['count1']
                    ress['table1']['non-collated']['table'] = ress['non-collated_table']
                    del ress['non-collated_table']
                    ress['table1']['cancelled']['value'] = ress['cancelled'][0]['count1']
                    del ress['cancelled'][0]['count1']
                    ress['table1']['cancelled']['table'] = ress['cancelled_table']
                    del ress['cancelled_table']
                    ress['table1']['over-voting']['value'] = ress['over-voting'][0]['count1']
                    del ress['over-voting'][0]['count1']
                    ress['table1']['over-voting']['table'] = ress['over-voting_table']
                    ress['table1']['Total Polling Units']['value'] = ress['total_pu']

                    del ress['over-voting'],ress['total_pu'],ress['collated'],ress['cancelled'],ress['over-voting_table']
                    ress['table2'] ={}

                    ress['table2']['NNPP'] ={"score":ress['scores'][0]['NNPP'],"ward_led":ress['Wards_led_NNPP'],"ward_led_table":ress['Wards_led_NNPP_table'],"lga_led":ress["Lga's_led_NNPP"],"lga_led_table":ress["Lga's_led_NNPP_table"]}
                    ress['table2']['APC'] ={"score":ress['scores'][0]['APC'],"ward_led":ress['Wards_led_APC'],"ward_led_table":ress['Wards_led_APC_table'],"lga_led":ress["Lga's_led_APC"],"lga_led_table":ress["Lga's_led_APC_table"]}
                    ress['table2']['PDP'] ={"score":ress['scores'][0]['PDP'],"ward_led":ress['Wards_led_PDP'],"ward_led_table":ress['Wards_led_PDP_table'],"lga_led":ress["Lga's_led_PDP"],"lga_led_table":ress["Lga's_led_PDP_table"]}
                    ress['table2']['ADP'] ={"score":ress['scores'][0]['ADP'],"ward_led":ress['Wards_led_ADP'],"ward_led_table":ress['Wards_led_ADP_table'],"lga_led":ress["Lga's_led_ADP"],"lga_led_table":ress["Lga's_led_ADP_table"]}
                    del ress['scores'],ress['Wards_led_NNPP'],ress['Wards_led_NNPP_table'],ress["Lga's_led_NNPP"],ress["Lga's_led_NNPP_table"]
                    del ress['Wards_led_APC'],ress['Wards_led_APC_table'],ress["Lga's_led_APC"],ress["Lga's_led_APC_table"]
                    del ress['Wards_led_PDP'],ress['Wards_led_PDP_table'],ress["Lga's_led_PDP"],ress["Lga's_led_PDP_table"]
                    del ress['Wards_led_ADP'],ress['Wards_led_ADP_table'],ress["Lga's_led_ADP"],ress["Lga's_led_ADP_table"]

                    
                    return ress
                
        


def ward_dashboard(type,constiuency_name):
     
     conditions_ward_rep = {
     
            "Registered Voters":f"""{presidential_table_ward_rep['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  house_ward_table where house_id={constiuency_name}""",
            "Accredited Voters":f"""{presidential_table_ward_rep['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  house_ward_table where house_id={constiuency_name}""",
            "Valid Voters":f"""{presidential_table_ward_rep['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  wt where house_id={constiuency_name} """,
            "slider_gragh":f"""{presidential_table_ward_rep['query']}  SELECT 
 NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM house 		
where house_id={constiuency_name} """,
            "collation_slider_message":f"""{presidential_table_ward_rep['query']}  select if (count(*)=0 ,'collation not started', 
 		if (count(*)=(select count(*) from house_ward_table where house_id={constiuency_name}), 'collation completed','collation in progress......')) 
 		from house_ward_table where (status='collated' or status='canceled') and house_id={constiuency_name}		
		 """,
            "collation_slider_value":f"""{presidential_table_ward_rep['query']}  select count(*) as count1 from house_ward_table where (status='collated' or status='canceled') and house_id={constiuency_name} """,
            "total_ward":f"""{presidential_table_ward_rep['query']} select count(*) AS count1 from house_ward_table where  house_id={constiuency_name} """ ,
            "collated":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from house_ward_table where status='collated' and house_id={constiuency_name} """,
            "collated_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,remarks from wt where status='collated' and house_id={constiuency_name} """,
            "non-collated":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from house_ward_table where status='non collated' and house_id={constiuency_name} """,
            "non-collated_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,remarks from wt where status='non collated' and house_id={constiuency_name} """,
            "cancelled":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from wt where status='canceled' and house_id={constiuency_name} """,
            "cancelled_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,remarks from wt where status='canceled' and house_id={constiuency_name} """,
            "over-voting":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from wt where over_vote_values>0 and house_id={constiuency_name} """,
            "over-voting_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from wt where over_vote_values>0 and house_id={constiuency_name} """,
            "scores": f"""{presidential_table_ward_rep['query']} select NNPP,APC,PDP,ADP from house where house_id={constiuency_name}  """,
  

            "Wards_led_NNPP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"   and house_id={constiuency_name}        """,
            "Wards_led_NNPP_table":f"""{presidential_table_ward_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" and house_id={constiuency_name}   """,
            "Lga's_led_NNPP":f"""{presidential_table_ward_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  and house_id={constiuency_name}      """,
            "Lga's_led_NNPP_table":f"""{presidential_table_ward_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" and house_id={constiuency_name}     """,
            
   
            
            "Wards_led_APC":f"""{presidential_table_ward_rep['query']}   select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="APC"   and house_id={constiuency_name}     """,
            "Wards_led_APC_table":f"""{presidential_table_ward_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"  and house_id={constiuency_name}   """,
            "Lga's_led_APC":f"""{presidential_table_ward_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"    and house_id={constiuency_name}       """,
            "Lga's_led_APC_table":f"""{presidential_table_ward_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"  and house_id={constiuency_name}    """,

            
            "Wards_led_PDP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="PDP" and house_id={constiuency_name}  """,
            "Wards_led_PDP_table":f"""{presidential_table_ward_rep['query']}    select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  and house_id={constiuency_name}     """,
            "Lga's_led_PDP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  and house_id={constiuency_name}          """,
            "Lga's_led_PDP_table":f"""{presidential_table_ward_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"    and house_id={constiuency_name}      """,
            

            "Wards_led_ADP":f"""{presidential_table_ward_rep['query']}       select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="ADP"  and house_id={constiuency_name}            """,
            "Wards_led_ADP_table":f"""{presidential_table_ward_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP"  and house_id={constiuency_name}   """,
            "Lga's_led_ADP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"     and house_id={constiuency_name}               """,
            "Lga's_led_ADP_table":f"""{presidential_table_ward_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" and house_id={constiuency_name}  """,
            "Party Led in Kano State":f"""{presidential_table_ward_rep['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1 and house_id={constiuency_name} 
         """
            

    }


     with get_db() as conn:
                cur = conn.cursor()
                key_values = []
                execute_queries = []


                if type =='gubernatorial':

                
                        for key,value in conditions_ward.items():
                            execute_queries.append(value)
                            key_values.append(key)
                        ress = {}
                        for index,sql in enumerate(execute_queries):
                                try:
                                    cur.execute(sql)
                                    results = cur.fetchall()
                                    ress[key_values[index]] = results
                                    
                                except:
                                    print('Skipped a sceanrio')

                        ress['table1'] ={"Total Wards":{},"collated":{},"non-collated":{},"cancelled":{},"over-voting":{}}
                        ress['table1']['collated']['value'] = ress['collated'][0]['count1']
                        del ress['collated'][0]['count1']
                        ress['table1']['collated']['table'] = ress['collated_table']
                        del ress['collated_table']
                        ress['table1']['non-collated']['value'] = ress['non-collated'][0]['count1']
                        del ress['non-collated'][0]['count1']
                        ress['table1']['non-collated']['table'] = ress['non-collated_table']
                        del ress['non-collated_table']
                        ress['table1']['cancelled']['value'] = ress['cancelled'][0]['count1']
                        del ress['cancelled'][0]['count1']
                        ress['table1']['cancelled']['table'] = ress['cancelled_table']
                        del ress['cancelled_table']
                        ress['table1']['over-voting']['value'] = ress['over-voting'][0]['count1']
                        del ress['over-voting'][0]['count1']
                        ress['table1']['over-voting']['table'] = ress['over-voting_table']
                        ress['table1']['Total Wards']['value'] = ress['total_ward']

                        del ress['over-voting'],ress['total_ward'],ress['collated'],ress['cancelled'],ress['over-voting_table']
                        ress['table2'] ={}

                        ress['table2']['NNPP'] ={"score":ress['scores'][0]['NNPP'],"ward_led":ress['Wards_led_NNPP'],"ward_led_table":ress['Wards_led_NNPP_table'],"lga_led":ress["Lga's_led_NNPP"],"lga_led_table":ress["Lga's_led_NNPP_table"]}
                        ress['table2']['APC'] ={"score":ress['scores'][0]['APC'],"ward_led":ress['Wards_led_APC'],"ward_led_table":ress['Wards_led_APC_table'],"lga_led":ress["Lga's_led_APC"],"lga_led_table":ress["Lga's_led_APC_table"]}
                        ress['table2']['PDP'] ={"score":ress['scores'][0]['PDP'],"ward_led":ress['Wards_led_PDP'],"ward_led_table":ress['Wards_led_PDP_table'],"lga_led":ress["Lga's_led_PDP"],"lga_led_table":ress["Lga's_led_PDP_table"]}
                        ress['table2']['ADP'] ={"score":ress['scores'][0]['ADP'],"ward_led":ress['Wards_led_ADP'],"ward_led_table":ress['Wards_led_ADP_table'],"lga_led":ress["Lga's_led_ADP"],"lga_led_table":ress["Lga's_led_ADP_table"]}
                        del ress['scores'],ress['Wards_led_NNPP'],ress['Wards_led_NNPP_table'],ress["Lga's_led_NNPP"],ress["Lga's_led_NNPP_table"]
                        del ress['Wards_led_APC'],ress['Wards_led_APC_table'],ress["Lga's_led_APC"],ress["Lga's_led_APC_table"]
                        del ress['Wards_led_PDP'],ress['Wards_led_PDP_table'],ress["Lga's_led_PDP"],ress["Lga's_led_PDP_table"]
                        del ress['Wards_led_ADP'],ress['Wards_led_ADP_table'],ress["Lga's_led_ADP"],ress["Lga's_led_ADP_table"]

                        
                        return ress
                        
        
                    
                
                    
                elif type =='house-of-assembly':
                    for key,value in conditions_ward_rep.items():
                            execute_queries.append(value)
                            key_values.append(key)
                    ress = {}
                    for index,sql in enumerate(execute_queries):
                            try:
                                cur.execute(sql)
                                results = cur.fetchall()
                                ress[key_values[index]] = results
                            except:
                                print('Skipped a sceanrio')

                    ress['table1'] ={"Total Wards":{},"collated":{},"non-collated":{},"cancelled":{},"over-voting":{}}
                    ress['table1']['collated']['value'] = ress['collated'][0]['count1']
                    del ress['collated'][0]['count1']
                    ress['table1']['collated']['table'] = ress['collated_table']
                    del ress['collated_table']
                    ress['table1']['non-collated']['value'] = ress['non-collated'][0]['count1']
                    del ress['non-collated'][0]['count1']
                    ress['table1']['non-collated']['table'] = ress['non-collated_table']
                    del ress['non-collated_table']
                    ress['table1']['cancelled']['value'] = ress['cancelled'][0]['count1']
                    del ress['cancelled'][0]['count1']
                    ress['table1']['cancelled']['table'] = ress['cancelled_table']
                    del ress['cancelled_table']
                    ress['table1']['over-voting']['value'] = ress['over-voting'][0]['count1']
                    del ress['over-voting'][0]['count1']
                    ress['table1']['over-voting']['table'] = ress['over-voting_table']
                    ress['table1']['Total Wards']['value'] = ress['total_ward']

                    del ress['over-voting'],ress['total_ward'],ress['collated'],ress['cancelled'],ress['over-voting_table']
                    ress['table2'] ={}

                    ress['table2']['NNPP'] ={"score":ress['scores'][0]['NNPP'],"ward_led":ress['Wards_led_NNPP'],"ward_led_table":ress['Wards_led_NNPP_table'],"lga_led":ress["Lga's_led_NNPP"],"lga_led_table":ress["Lga's_led_NNPP_table"]}
                    ress['table2']['APC'] ={"score":ress['scores'][0]['APC'],"ward_led":ress['Wards_led_APC'],"ward_led_table":ress['Wards_led_APC_table'],"lga_led":ress["Lga's_led_APC"],"lga_led_table":ress["Lga's_led_APC_table"]}
                    ress['table2']['PDP'] ={"score":ress['scores'][0]['PDP'],"ward_led":ress['Wards_led_PDP'],"ward_led_table":ress['Wards_led_PDP_table'],"lga_led":ress["Lga's_led_PDP"],"lga_led_table":ress["Lga's_led_PDP_table"]}
                    ress['table2']['ADP'] ={"score":ress['scores'][0]['ADP'],"ward_led":ress['Wards_led_ADP'],"ward_led_table":ress['Wards_led_ADP_table'],"lga_led":ress["Lga's_led_ADP"],"lga_led_table":ress["Lga's_led_ADP_table"]}
                    
                    del ress['scores'],ress['Wards_led_NNPP'],ress['Wards_led_NNPP_table'],ress["Lga's_led_NNPP"],ress["Lga's_led_NNPP_table"]
                    del ress['Wards_led_APC'],ress['Wards_led_APC_table'],ress["Lga's_led_APC"],ress["Lga's_led_APC_table"]
                    del ress['Wards_led_PDP'],ress['Wards_led_PDP_table'],ress["Lga's_led_PDP"],ress["Lga's_led_PDP_table"]
                    del ress['Wards_led_ADP'],ress['Wards_led_ADP_table'],ress["Lga's_led_ADP"],ress["Lga's_led_ADP_table"]

                    
                    return ress
    


def lga_dashboard(type,constiuency_name):
       
        conditions_lga_rep = {
     
            "Registered Voters":f"""{presidential_table_lga_rep['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  house_lga_table where house_id={constiuency_name} """,
            "Accredited Voters":f"""{presidential_table_lga_rep['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  house_lga_table where house_id={constiuency_name} """,
            "Valid Voters":f"""{presidential_table_lga_rep['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  lgat where house_id={constiuency_name}""",
            "slider_gragh":f"""{presidential_table_lga_rep['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
            APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
            PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
            ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
            (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
            IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM house where house_id={constiuency_name}		
            """,
                        "collation_slider_message":f"""{presidential_table_lga_rep['query']}  select if (count(*)=0 ,'collation not started', 
 		if (count(*)=(select count(*) from house_lga_table where house_id={constiuency_name}), 'collation completed','collation in progress......')) 
 		from house_lga_table where (status='collated' or status='canceled')	and house_id={constiuency_name}					
                    """,
                        "collation_slider_value":f"""{presidential_table_lga_rep['query']}  select count(*) as count1 from house_lga_table where (status='collated' or status='canceled') and house_id={constiuency_name} """,
                        "total_lga":f"""{presidential_table_lga_rep['query']} select count(*) AS count1 from house_lga_table where house_id={constiuency_name} """ ,
                        "collated":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from house_lga_table where status='collated' and house_id={constiuency_name} """,
                        "collated_table":f"""{presidential_table_lga_rep['query']} select lga_name,remarks from lgat where status='collated' and house_id={constiuency_name} """,
                        "non-collated":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from house_lga_table where status='non collated' and house_id={constiuency_name} """,
                        "non-collated_table":f"""{presidential_table_lga_rep['query']} select lga_name,remarks from lgat where status='non collated' and house_id={constiuency_name} """,
                        "cancelled":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from lgat where status='canceled' and house_id={constiuency_name} """,
                        "cancelled_table":f"""{presidential_table_lga_rep['query']} select lga_name,remarks from lgat where status='canceled' and house_id={constiuency_name} """,
                        "over-voting":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from lgat where over_vote_values>0 and house_id={constiuency_name} """,
                        "over-voting_table":f"""{presidential_table_lga_rep['query']} select lga_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from lgat where over_vote_values>0 and house_id={constiuency_name}""",
                        "scores": f"""{presidential_table_lga_rep['query']} select NNPP,APC,PDP,ADP from house where house_id={constiuency_name} """,
            

            
                        "Lga's_led_NNPP":f"""{presidential_table_lga_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  and house_id={constiuency_name}     """,
                        "Lga's_led_NNPP_table":f"""{presidential_table_lga_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
            WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  and house_id={constiuency_name}   """,
                        
            

                        
                        "Lga's_led_APC":f"""{presidential_table_lga_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"   and house_id={constiuency_name}       """,
                        "Lga's_led_APC_table":f"""{presidential_table_lga_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
            WHERE row_num<2 and total_valid_votes>0  AND party="APC"   and house_id={constiuency_name}  """,

                        

                        
                        "Lga's_led_PDP":f"""{presidential_table_lga_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP" and house_id={constiuency_name}          """,
                        "Lga's_led_PDP_table":f"""{presidential_table_lga_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
            WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  and house_id={constiuency_name}       """,
                        

                    
                        "Lga's_led_ADP":f"""{presidential_table_lga_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"   and house_id={constiuency_name}                """,
                        "Lga's_led_ADP_table":f"""{presidential_table_lga_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
            WHERE row_num<2 and total_valid_votes>0  AND party="ADP"  and house_id={constiuency_name} """,
                        "Party Led in Kano State":f"""{presidential_table_lga_rep['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1 and house_id={constiuency_name}
                    """
                        

                }

        with get_db() as conn:
                cur = conn.cursor()
                key_values = []
                execute_queries = []

   





                if type =='gubernatorial':

                
                        for key,value in conditions_lga.items():
                            execute_queries.append(value)
                            key_values.append(key)
                        ress = {}
                        for index,sql in enumerate(execute_queries):
                                try:
                                    cur.execute(sql)
                                    results = cur.fetchall()
                                    ress[key_values[index]] = results
                                    
                                except:
                                    print('Skipped a sceanrio')

                        ress['table1'] ={"Total Lgas":{},"collated":{},"non-collated":{},"cancelled":{},"over-voting":{}}
                        ress['table1']['collated']['value'] = ress['collated'][0]['count1']
                        del ress['collated'][0]['count1']
                        ress['table1']['collated']['table'] = ress['collated_table']
                        del ress['collated_table']
                        ress['table1']['non-collated']['value'] = ress['non-collated'][0]['count1']
                        del ress['non-collated'][0]['count1']
                        ress['table1']['non-collated']['table'] = ress['non-collated_table']
                        del ress['non-collated_table']
                        ress['table1']['cancelled']['value'] = ress['cancelled'][0]['count1']
                        del ress['cancelled'][0]['count1']
                        ress['table1']['cancelled']['table'] = ress['cancelled_table']
                        del ress['cancelled_table']
                        ress['table1']['over-voting']['value'] = ress['over-voting'][0]['count1']
                        del ress['over-voting'][0]['count1']
                        ress['table1']['over-voting']['table'] = ress['over-voting_table']
                        ress['table1']['Total Lgas']['value'] = ress['total_lga']

                        del ress['over-voting'],ress['total_lga'],ress['collated'],ress['cancelled'],ress['over-voting_table']
                        ress['table2'] ={}

                        ress['table2']['NNPP'] ={"score":ress['scores'][0]['NNPP'],"lga_led":ress["Lga's_led_NNPP"],"lga_led_table":ress["Lga's_led_NNPP_table"]}
                        ress['table2']['APC'] ={"score":ress['scores'][0]['APC'],"lga_led":ress["Lga's_led_APC"],"lga_led_table":ress["Lga's_led_APC_table"]}
                        ress['table2']['PDP'] ={"score":ress['scores'][0]['PDP'],"lga_led":ress["Lga's_led_PDP"],"lga_led_table":ress["Lga's_led_PDP_table"]}
                        ress['table2']['ADP'] ={"score":ress['scores'][0]['ADP'],"lga_led":ress["Lga's_led_ADP"],"lga_led_table":ress["Lga's_led_ADP_table"]}
                        del ress['scores'],ress["Lga's_led_NNPP"],ress["Lga's_led_NNPP_table"]
                        del ress["Lga's_led_APC"],ress["Lga's_led_APC_table"]
                        del ress["Lga's_led_PDP"],ress["Lga's_led_PDP_table"]
                        del ress["Lga's_led_ADP"],ress["Lga's_led_ADP_table"]

                        
                        return ress
              
                    
                
                    
                elif type =='house-of-assembly':
                    for key,value in conditions_lga_rep.items():
                            execute_queries.append(value)
                            key_values.append(key)
                    ress = {}
                    for index,sql in enumerate(execute_queries):
                            try:
                                cur.execute(sql)
                                results = cur.fetchall()
                                ress[key_values[index]] = results
                                
                            except:
                                print('Skipped a sceanrio')

                    ress['table1'] ={"Total Lgas":{},"collated":{},"non-collated":{},"cancelled":{},"over-voting":{}}
                    ress['table1']['collated']['value'] = ress['collated'][0]['count1']
                    del ress['collated'][0]['count1']
                    ress['table1']['collated']['table'] = ress['collated_table']
                    del ress['collated_table']
                    ress['table1']['non-collated']['value'] = ress['non-collated'][0]['count1']
                    del ress['non-collated'][0]['count1']
                    ress['table1']['non-collated']['table'] = ress['non-collated_table']
                    del ress['non-collated_table']
                    ress['table1']['cancelled']['value'] = ress['cancelled'][0]['count1']
                    del ress['cancelled'][0]['count1']
                    ress['table1']['cancelled']['table'] = ress['cancelled_table']
                    del ress['cancelled_table']
                    ress['table1']['over-voting']['value'] = ress['over-voting'][0]['count1']
                    del ress['over-voting'][0]['count1']
                    ress['table1']['over-voting']['table'] = ress['over-voting_table']
                    ress['table1']['Total Lgas']['value'] = ress['total_lga']

                    del ress['over-voting'],ress['total_lga'],ress['collated'],ress['cancelled'],ress['over-voting_table']
                    ress['table2'] ={}

                    ress['table2']['NNPP'] ={"score":ress['scores'][0]['NNPP'],"lga_led":ress["Lga's_led_NNPP"],"lga_led_table":ress["Lga's_led_NNPP_table"]}
                    ress['table2']['APC'] ={"score":ress['scores'][0]['APC'],"lga_led":ress["Lga's_led_APC"],"lga_led_table":ress["Lga's_led_APC_table"]}
                    ress['table2']['PDP'] ={"score":ress['scores'][0]['PDP'],"lga_led":ress["Lga's_led_PDP"],"lga_led_table":ress["Lga's_led_PDP_table"]}
                    ress['table2']['ADP'] ={"score":ress['scores'][0]['ADP'],"lga_led":ress["Lga's_led_ADP"],"lga_led_table":ress["Lga's_led_ADP_table"]}
                    del ress['scores'],ress["Lga's_led_NNPP"],ress["Lga's_led_NNPP_table"]
                    del ress["Lga's_led_APC"],ress["Lga's_led_APC_table"]
                    del ress["Lga's_led_PDP"],ress["Lga's_led_PDP_table"]
                    del ress["Lga's_led_ADP"],ress["Lga's_led_ADP_table"]

                    
                    return ress
    



def constituency_dashboard(constiuency_name):
     with get_db() as conn:
                cur = conn.cursor()
                key_values = []
                execute_queries = []

                conditions_const_rep = {
         
           "slider_gragh": f"""{presidential_table_const_rep['query']}  select house_code, house_name,  NNPP, APC,  PDP,   LP, AA,  AAC, ADC,  A,  ADP,   APGA,  APM,  APP,  BP,  NRM,  PRP,  SDP,  YPP,  ZLP, 
   		 Total_Registered_voters,Total_Accredited_voters,total_valid_votes,Total_Rejected_votes,total_vote_casted,remarks 
   		from house WHERE house_id={constiuency_name} """,
        

    }
                for key,value in conditions_const_rep.items():
                    execute_queries.append(value)
                    key_values.append(key)
                ress = {}
                for index,sql in enumerate(execute_queries):
                        try:
                            cur.execute(sql)
                            results = cur.fetchall()
                            ress[key_values[index]] = results
                            
                        except:
                            print('Skipped a sceanrio')

                
                return ress

def state_dashboard():
       with get_db() as conn:
                cur = conn.cursor()
                key_values = []
                execute_queries = []
                
                for key,value in conditions_state.items():
                    execute_queries.append(value)
                    key_values.append(key)
                ress = {}
                for index,sql in enumerate(execute_queries):
                        try:
                            cur.execute(sql)
                            results = cur.fetchall()
                            ress[key_values[index]] = results
                            
                        except:
                            print('Skipped a sceanrio')

                
                return ress
        
                        

      
    

      
def place(user):
    pollingUnit = user['pollingUnit']
    ward = user['ward']
    lga = user['lga']
    state =  user['state']
    country =1
    role = user['role']
    with get_db() as conn:
        cur = conn.cursor()

        if role == "pns":
                
                sql = f"""select distinct country_name from country_result_table Where country_id = {country} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')
        
        elif role == "pss":
                
                sql = f"""select distinct state_name from state_result_table Where country_id={country} and state_id={state}  """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')

        elif role == "pls":
        
                sql = f"""select distinct lga_name from lga_result_table Where country_id={country} and state_id={state} and lga_id={lga}  """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')
        
        elif role == "pws":
        
                sql = f"""select distinct ward_name from ward_result_table Where country_id={country} and state_id={state} and lga_id={lga} and ward_id ={ward} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')
        
        elif role == "ppa":
        
                sql = f"""select distinct pu_name from pu_result_table Where country_id={country} and state_id={state} and lga_id={lga} and ward_id ={ward} and pu_id = {pollingUnit} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')

        elif role == "sss":
        
                sql = f"""select distinct state_name from sen_district_table Where state_id = {state} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')
        
        elif role == "sds":
                #  constituency = user['constituency']
                district = user['district']
        
                sql = f"""select distinct district_name from sen_district_table Where state_id={state} and district_id = {district} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')
        

        elif role == "rss":
        
                sql = f"""select distinct state_name from rep_constituency_table Where state_id = {state} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')
        
        elif role == "rcs":
                constituency = user['constituency']
        
                sql = f"""select distinct constituency_name from rep_constituency_table Where state_id={state} and const_id = {constituency} """
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    return results
                except:
                    print('improper input')

        
        
        
        



    

