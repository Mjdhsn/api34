conditions_pu_rep = {
     
            "Registered Voters":f"""{presidential_table_pu_rep['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  house_pu_table""",
            "Accredited Voters":f"""{presidential_table_pu_rep['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  house_pu_table""",
            "Valid Voters":f"""{presidential_table_pu_rep['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  pu """,
            "slider_gragh":f"""{presidential_table_pu_rep['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_pu_rep['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=11212, 'collation completed','collation in progress......')) as message 
 		from house_pu_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_pu_rep['query']}  select count(*) as count1 from house_pu_table where (status='collated' or status='canceled') """,
            "total_pu":f"""{presidential_table_pu_rep['query']} select count(*) AS count1 from house_pu_table""" ,
            "collated":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from house_pu_table where status='collated'""",
            "collated_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='collated'""",
            "non-Collated":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from house_pu_table where status='non collated'""",
            "non-collated_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='non collated'""",
            "cancelled":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from pu where status='canceled'""",
            "cancelled_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,remarks from pu where status='canceled'""",
            "over-voting":f"""{presidential_table_pu_rep['query']} select count(*) as count1 from pu where over_vote_values>0 """,
            "over-voting_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code,pu_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from pu where over_vote_values>0""",
            "scores": f"""{presidential_table_pu_rep['query']} select NNPP,APC,PDP,ADP from st """,
            
            "PU_won_NNPP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" """,
           
           
            "PU_won_NNPP_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP" """,


            "Wards_led_NNPP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"          """,
            "Wards_led_NNPP_table":f"""{presidential_table_pu_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  """,
            "Lga's_led_NNPP":f"""{presidential_table_pu_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"       """,
            "Lga's_led_NNPP_table":f"""{presidential_table_pu_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"     """,
            "PU_won_APC":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="APC" """,
            "PU_won_APC_table": f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
WHERE row_num<2 and total_valid_votes>0  AND party="APC" """,
            "Wards_led_APC":f"""{presidential_table_pu_rep['query']}   select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="APC"       """,
            "Wards_led_APC_table":f"""{presidential_table_pu_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"    """,
            "Lga's_led_APC":f"""{presidential_table_pu_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"          """,
            "Lga's_led_APC_table":f"""{presidential_table_pu_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"     """,
            "PU_won_PDP":f"""{presidential_table_pu_rep['query']} select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="PDP" """,
            "PU_won_PDP_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP" """,
            "Wards_led_PDP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  """,
            "Wards_led_PDP_table":f"""{presidential_table_pu_rep['query']}    select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"      """,
            "Lga's_led_PDP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"           """,
            "Lga's_led_PDP_table":f"""{presidential_table_pu_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"         """,
            "PU_won_ADP":f"""{presidential_table_pu_rep['query']}   select count(*) AS count1 from win_pu WHERE row_num<2 and total_valid_votes>0  AND party="ADP"
 """,
            "PU_won_ADP_table":f"""{presidential_table_pu_rep['query']} select lga_name,ward_name,pu_code, pu_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_pu 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Wards_led_ADP":f"""{presidential_table_pu_rep['query']}       select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="ADP"             """,
            "Wards_led_ADP_table":f"""{presidential_table_pu_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP"    """,
            "Lga's_led_ADP":f"""{presidential_table_pu_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"                   """,
            "Lga's_led_ADP_table":f"""{presidential_table_pu_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Party Led in the state":f"""{presidential_table_pu_rep['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1
         """
            

    }
conditions_ward_rep = {
     
            "Registered Voters":f"""{presidential_table_ward_rep['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  house_ward_table""",
            "Accredited Voters":f"""{presidential_table_ward_rep['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  house_ward_table""",
            "Valid Voters":f"""{presidential_table_ward_rep['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  wt """,
            "slider_gragh":f"""{presidential_table_ward_rep['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_ward_rep['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=484, 'collation completed','collation in progress......')) as message 
 		from house_ward_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_ward_rep['query']}  select count(*) as count1 from house_ward_table where (status='collated' or status='canceled') """,
            "total_ward":f"""{presidential_table_ward_rep['query']} select count(*) AS count1 from house_ward_table""" ,
            "collated":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from house_ward_table where status='collated'""",
            "collated_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,remarks from wt where status='collated'""",
            "non-Collated":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from house_ward_table where status='non collated'""",
            "non-collated_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,remarks from wt where status='non collated'""",
            "cancelled":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from wt where status='canceled'""",
            "cancelled_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,remarks from wt where status='canceled'""",
            "over-voting":f"""{presidential_table_ward_rep['query']} select count(*) as count1 from wt where over_vote_values>0 """,
            "over-voting_table":f"""{presidential_table_ward_rep['query']} select lga_name,ward_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from wt where over_vote_values>0""",
            "scores": f"""{presidential_table_ward_rep['query']} select NNPP,APC,PDP,ADP from st """,
  

            "Wards_led_NNPP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"          """,
            "Wards_led_NNPP_table":f"""{presidential_table_ward_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"  """,
            "Lga's_led_NNPP":f"""{presidential_table_ward_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"       """,
            "Lga's_led_NNPP_table":f"""{presidential_table_ward_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"     """,
            
   
            
            "Wards_led_APC":f"""{presidential_table_ward_rep['query']}   select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="APC"       """,
            "Wards_led_APC_table":f"""{presidential_table_ward_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"    """,
            "Lga's_led_APC":f"""{presidential_table_ward_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"          """,
            "Lga's_led_APC_table":f"""{presidential_table_ward_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"     """,

            
            "Wards_led_PDP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="PDP"  """,
            "Wards_led_PDP_table":f"""{presidential_table_ward_rep['query']}    select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"      """,
            "Lga's_led_PDP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"           """,
            "Lga's_led_PDP_table":f"""{presidential_table_ward_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"         """,
            

            "Wards_led_ADP":f"""{presidential_table_ward_rep['query']}       select count(*) AS count1 from win_ward WHERE row_num<2 and total_valid_votes>0  AND party="ADP"             """,
            "Wards_led_ADP_table":f"""{presidential_table_ward_rep['query']}  select lga_name,ward_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_ward 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP"    """,
            "Lga's_led_ADP":f"""{presidential_table_ward_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"                   """,
            "Lga's_led_ADP_table":f"""{presidential_table_ward_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Party Led in the state":f"""{presidential_table_ward_rep['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1
         """
            

    }

conditions_lga_rep = {
     
            "Registered Voters":f"""{presidential_table_lga_rep['query']} SELECT coalesce(sum(Total_Registered_voters),0) AS count1  FROM  house_lga_table""",
            "Accredited Voters":f"""{presidential_table_lga_rep['query']} SELECT coalesce(sum(Total_Accredited_voters),0) AS count1  FROM  house_lga_table""",
            "Valid Voters":f"""{presidential_table_lga_rep['query']} SELECT coalesce(sum(total_vote_casted),0)  AS count1 FROM  lgat """,
            "slider_gragh":f"""{presidential_table_lga_rep['query']}  SELECT NNPP,  IF(total_vote_casted>0, concat(round(NNPP/total_vote_casted*100,2),'%'), '0.00%') as percentage_NNPP, 
 APC, IF(total_vote_casted>0, concat(round(APC/total_vote_casted*100,2),'%'), '0.00%') as percentage_APC,
 PDP, IF(total_vote_casted>0, concat(round(PDP/total_vote_casted*100,2),'%'), '0.00%') as percentage_PDP, 
 ADP, IF(total_vote_casted>0, concat(round(ADP/total_vote_casted*100,2),'%'), '0.00%') as percentage_LP,
 (A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP) AS OTHERS,
 IF(total_vote_casted>0,concat(round((A + AA + ADP + APP + AAC + ADC  + APGA + APM + BP  + NRM + NNPP + PRP + SDP + YPP + ZLP)/total_vote_casted*100,2),'%'),'0.00%') as percentage_others FROM st		
""",
            "collation_slider_message":f"""{presidential_table_lga_rep['query']} select if (count(*)=0 ,'collation not started', 
 		if (count(*)=774, 'collation completed','collation in progress......')) as message 
 		from house_lga_table where (status='collated' or status='canceled')			
		 """,
            "collation_slider_value":f"""{presidential_table_lga_rep['query']}  select count(*) as count1 from house_lga_table where (status='collated' or status='canceled') """,
            "total_lga":f"""{presidential_table_lga_rep['query']} select count(*) AS count1 from house_lga_table""" ,
            "collated":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from house_lga_table where status='collated'""",
            "collated_table":f"""{presidential_table_lga_rep['query']} select lga_name,remarks from lgat where status='collated'""",
            "non-Collated":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from house_lga_table where status='non collated'""",
            "non-collated_table":f"""{presidential_table_lga_rep['query']} select lga_name,remarks from lgat where status='non collated'""",
            "cancelled":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from lgat where status='canceled'""",
            "cancelled_table":f"""{presidential_table_lga_rep['query']} select lga_name,remarks from lgat where status='canceled'""",
            "over-voting":f"""{presidential_table_lga_rep['query']} select count(*) as count1 from lgat where over_vote_values>0 """,
            "over-voting_table":f"""{presidential_table_lga_rep['query']} select lga_name,Total_Registered_voters,Total_Accredited_voters, total_valid_votes,over_vote_values, remarks from lgat where over_vote_values>0""",
            "scores": f"""{presidential_table_lga_rep['query']} select NNPP,APC,PDP,ADP from st """,
  

 
            "Lga's_led_NNPP":f"""{presidential_table_lga_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"       """,
            "Lga's_led_NNPP_table":f"""{presidential_table_lga_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="NNPP"     """,
            
   

            
            "Lga's_led_APC":f"""{presidential_table_lga_rep['query']}     select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="APC"          """,
            "Lga's_led_APC_table":f"""{presidential_table_lga_rep['query']}   select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="APC"     """,

            

            
            "Lga's_led_PDP":f"""{presidential_table_lga_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="PDP"           """,
            "Lga's_led_PDP_table":f"""{presidential_table_lga_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="PDP"         """,
            

           
            "Lga's_led_ADP":f"""{presidential_table_lga_rep['query']}  select count(*) AS count1 from win_lga WHERE row_num<2 and total_valid_votes>0  AND party="ADP"                   """,
            "Lga's_led_ADP_table":f"""{presidential_table_lga_rep['query']}  select lga_name, votes as Scores, total_vote_casted,Total_Registered_voters,Total_Accredited_voters, percentage_votes from win_lga 
WHERE row_num<2 and total_valid_votes>0  AND party="ADP" """,
            "Party Led in the state":f"""{presidential_table_lga_rep['query']}    SELECT ROW_NUMBER() OVER(PARTITION BY state_name ORDER BY votes DESC) AS row_num,party FROM win_state  where row_num=1
         """
            

    }
