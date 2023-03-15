

presidential_table_pu = {
"query": f"""

WITH pu AS

    (SELECT *, (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP) AS total_valid_votes,

          (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes)
          AS total_vote_casted, 
          
          IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
              YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
              (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
               Total_Rejected_votes) - Total_Accredited_voters,
               IF( Total_Accredited_voters  > Total_Registered_voters,
               Total_Accredited_voters - Total_Registered_voters, 0)
                 ) AS over_vote_values,

         IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters and 
                   Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
          	    IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
                   'Over Votting! Because total votes casted are greater than total accredited voters',  
                   IF( Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total accredited voters are greater than total registered voters', 
                   IF (status='canceled','canceled',
                   IF(A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP>0,'OK','non collated')
                   )))) AS remarks,     
                 
        
             IF (status='canceled','canceled',
             IF (Total_Registered_voters>0 and
            	 A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes>0,             
                 CONCAT(ROUND((A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
                 Total_Rejected_votes)/Total_Registered_voters *100,2),'%'), 
                 if (Total_Registered_voters<=0,'Warning!! total registered voters = 0','not collated')) 
                 
                 ) AS percentage_voters_turnout


            FROM house_pu_table hpt),

 wt as
		(SELECT house_id, house_name, house_code, state_id, state_name, lga_id, lga_name, ward_id, ward_name,
			sum(A) AS A, sum(AA) AS AA, sum(AAC) AS AAC, 
			sum(ADC) AS ADC, sum(ADP) AS ADP, sum(APC) AS APC, sum(APGA) AS APGA,
			sum(APM) AS APM, sum(APP) AS APP, sum(BP) AS BP, sum(LP) AS LP,
			sum(NRM) AS NRM, sum(NNPP) as NNPP, sum(PDP) AS PDP, sum(PRP) AS PRP, 
			sum(SDP) AS SDP, sum(YPP) AS YPP, sum(ZLP) AS ZLP, 
			sum(Total_Rejected_votes) AS Total_Rejected_votes, sum(Total_Registered_voters) AS Total_Registered_voters,
			sum(Total_Accredited_voters) AS Total_Accredited_voters, 
			
		   (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)) AS total_valid_votes,

          (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))
          AS total_vote_casted, 
		
 		 IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > Total_Accredited_voters ,
            (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) - sum(Total_Accredited_voters),
               IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
               sum(Total_Accredited_voters) - sum(Total_Registered_voters), 0)
                 ) AS over_vote_values,
                 
IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) and 
            sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
         IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) ,
            'Over Votting! Because total votes casted are greater than total accredited voters',  
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
           'Over Votting! Because total accredited voters are greater than total registered voters', 
        IF(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)>0,'OK','non collated')
                   ))) AS remarks, 
             
 IF (sum(Total_Registered_voters)>0 and
           sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)>0,             
           CONCAT(ROUND((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))/sum(Total_Registered_voters) *100,2),'%'), 
       IF (sum(Total_Registered_voters)<=0,'Warning!! total registered voters = 0','not collated')) 
          AS percentage_voters_turnout
                 
        	FROM house_pu_table hpt  group by house_id, lga_id, ward_id) ,

lgat AS
		(select house_id, house_name, house_code, state_id, state_name, lga_id, lga_name, sum(A) AS A, sum(AA) AS AA, sum(AAC) AS AAC, 
			sum(ADC) AS ADC, sum(ADP) AS ADP, sum(APC) AS APC, sum(APGA) AS APGA,
			sum(APM) AS APM, sum(APP) AS APP, sum(BP) AS BP, sum(LP) AS LP,
			sum(NRM) AS NRM, sum(NNPP) as NNPP, sum(PDP) AS PDP, sum(PRP) AS PRP, 
			sum(SDP) AS SDP, sum(YPP) AS YPP, sum(ZLP) AS ZLP, 
			sum(Total_Rejected_votes) AS Total_Rejected_votes, sum(Total_Registered_voters) AS Total_Registered_voters,
			sum(Total_Accredited_voters) AS Total_Accredited_voters,
			
 			(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
          	sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)) AS total_valid_votes,

          (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
           sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))
          AS total_vote_casted, 
		
 		 IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > Total_Accredited_voters ,
            (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) - sum(Total_Accredited_voters),
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            sum(Total_Accredited_voters) - sum(Total_Registered_voters), 0)
                 ) AS over_vote_values,
                 
		IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) and 
            sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
         IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) ,
            'Over Votting! Because total votes casted are greater than total accredited voters',  
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
           'Over Votting! Because total accredited voters are greater than total registered voters', 
        IF(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)>0,'OK','non collated')
                   ))) AS remarks, 
             
 		IF (sum(Total_Registered_voters)>0 and
           sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)>0,             
           CONCAT(ROUND((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))/sum(Total_Registered_voters) *100,2),'%'), 
       IF (sum(Total_Registered_voters)<=0,'Warning!! total registered voters = 0','not collated')) 
       AS percentage_voters_turnout              
       FROM wt GROUP BY house_id, lga_id),
        
house AS
		(select house_id,house_name, house_code,state_id,state_name, sum(A) AS A, sum(AA) AS AA, sum(AAC) AS AAC, 
			sum(ADC) AS ADC, sum(ADP) AS ADP, sum(APC) AS APC, sum(APGA) AS APGA,
			sum(APM) AS APM, sum(APP) AS APP, sum(BP) AS BP, sum(LP) AS LP,
			sum(NRM) AS NRM, sum(NNPP) as NNPP, sum(PDP) AS PDP, sum(PRP) AS PRP, 
			sum(SDP) AS SDP, sum(YPP) AS YPP, sum(ZLP) AS ZLP, 
			sum(Total_Rejected_votes) AS Total_Rejected_votes, sum(Total_Registered_voters) AS Total_Registered_voters,
			sum(Total_Accredited_voters) AS Total_Accredited_voters,

			(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
          	sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)) AS total_valid_votes,

          (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
           sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))
          AS total_vote_casted, 
		
 		 IF (((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) > Total_Accredited_voters) ,
            (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) - sum(Total_Accredited_voters),
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            sum(Total_Accredited_voters) - sum(Total_Registered_voters), 0)
                 ) AS over_vote_values,
                 
		IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) and 
            sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
         IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) ,
            'Over Votting! Because total votes casted are greater than total accredited voters',  
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
           'Over Votting! Because total accredited voters are greater than total registered voters', 
        IF(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)>0,'OK','non collated')
                   ))) AS remarks, 
             
 		IF (sum(Total_Registered_voters)>0 and
           sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)>0,             
           CONCAT(ROUND((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))/sum(Total_Registered_voters) *100,2),'%'), 
       IF (sum(Total_Registered_voters)<=0,'Warning!! total registered voters = 0','not collated')) 
       AS percentage_voters_turnout        
       FROM lgat GROUP BY house_id),
        
 
win AS
         (SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM pu 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM pu
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM pu
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM pu
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM pu  
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM pu  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name,pu_code, pu_name,Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM pu ),

win_w AS
         (SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM wt 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM wt 
          UNION
       	  SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM wt  
          UNION
		  SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM wt   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM wt  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM wt   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM wt   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM wt 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM wt  ),

win_l AS
         (SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM lgat  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM lgat   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM lgat  ),
          
win_h AS
         (SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM house   
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM house   ),
          

win_pu AS
           (SELECT state_id,house_id,house_code,house_name, lga_id, ward_id,state_name,lga_name, ward_name,pu_code,pu_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		over_vote_values,total_vote_casted,total_valid_votes,remarks,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY pu_code ORDER BY votes DESC) AS row_num FROM win),
                
 win_ward AS
           (SELECT state_id,house_id,house_code,house_name, lga_id, ward_id,state_name,lga_name, ward_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY ward_name ORDER BY votes DESC) AS row_num FROM win_w),
                
win_lga AS
           (SELECT state_id,house_id,house_code,house_name, lga_id,state_name,lga_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY lga_name ORDER BY votes DESC) AS row_num FROM win_l),
                
win_house AS
           (SELECT state_id,house_id,house_code,house_name,state_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY house_code ORDER BY votes DESC) AS row_num FROM win_h),

non_collated_ward AS 
			(SELECT distinct ward_id,state_id,house_id,house_code,house_name,lga_id,state_name,lga_name, ward_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id, ward_id) AS Total_Registered_voters,
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id, ward_id) AS total FROM pu),   -- 7. non collated wards
			
non_collated_lga AS 
			(SELECT DISTINCT  lga_id, state_id,house_id,house_code,house_name,state_name,lga_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM pu),

non_collated_house AS 
			(SELECT DISTINCT state_id,house_id,house_code,house_name,state_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters, 
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM pu),		
		
collated_ward AS 
			(SELECT distinct ward_id,state_id,house_id,house_code,house_name,lga_id,state_name,lga_name, ward_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id, ward_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id, ward_id) AS total FROM pu),

collated_lga AS
			(SELECT distinct lga_id,state_id,house_id,house_code,house_name,state_name,lga_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM pu),

collated_house AS
			(SELECT distinct state_id,house_id,house_code,house_name,state_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM pu)              
"""

}

presidential_table_ward ={
	
	"query": f"""
WITH wt AS

    (SELECT *, (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP) AS total_valid_votes,

          (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes)
          AS total_vote_casted, 
          
          IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
              YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
              (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
               Total_Rejected_votes) - Total_Accredited_voters,
               IF( Total_Accredited_voters  > Total_Registered_voters,
               Total_Accredited_voters - Total_Registered_voters, 0)
                 ) AS over_vote_values,
                 
         IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters and 
                   Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
          	    IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
                   'Over Votting! Because total votes casted are greater than total accredited voters',  
                   IF( Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total accredited voters are greater than total registered voters', 
                   IF (status='canceled','canceled',
                   IF(A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP>0,'OK','non collated')
                   )))) AS remarks,                    
                 
                 
             IF (status='canceled','canceled',
             IF (Total_Registered_voters>0 and
            	 A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes>0,             
                 CONCAT(ROUND((A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
                 Total_Rejected_votes)/Total_Registered_voters *100,2),'%'), 
                 if (Total_Registered_voters<=0,'Warning!! total registered voters = 0','not collated')) 
                 
                 ) AS percentage_voters_turnout


            FROM house_ward_table),

lgat AS
		(SELECT state_id,house_id,house_code,house_name, state_name, lga_id, lga_name, sum(A) AS A, sum(AA) AS AA, sum(AAC) AS AAC, 
			sum(ADC) AS ADC, sum(ADP) AS ADP, sum(APC) AS APC, sum(APGA) AS APGA,
			sum(APM) AS APM, sum(APP) AS APP, sum(BP) AS BP, sum(LP) AS LP,
			sum(NRM) AS NRM, sum(NNPP) as NNPP, sum(PDP) AS PDP, sum(PRP) AS PRP, 
			sum(SDP) AS SDP, sum(YPP) AS YPP, sum(ZLP) AS ZLP, 
			sum(Total_Rejected_votes) AS Total_Rejected_votes, sum(Total_Registered_voters) AS Total_Registered_voters,
			sum(Total_Accredited_voters) AS Total_Accredited_voters,
			
 			(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
          	sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)) AS total_valid_votes,

          (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
           sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))
          AS total_vote_casted, 
		
 		 IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > Total_Accredited_voters ,
            (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) - sum(Total_Accredited_voters),
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            sum(Total_Accredited_voters) - sum(Total_Registered_voters), 0)
                 ) AS over_vote_values,
                 
         IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters and 
                   Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
          			IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
                   'Over Votting! Because total votes casted are greater than total accredited voters',  
                   IF( Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total accredited voters are greater than total registered voters', 
                   IF (status='canceled','canceled',
                   IF (status='non collated','non collated',
                   IF(A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP>0,'OK','check manually, please..')
                   ))))) AS remarks,     
             
 		IF (sum(Total_Registered_voters)>0 and
           sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)>0,             
           CONCAT(ROUND((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))/sum(Total_Registered_voters) *100,2),'%'), 
       IF (sum(Total_Registered_voters)<=0,'Warning!! total registered voters = 0','not collated')) 
       AS percentage_voters_turnout              
       FROM wt GROUP BY house_id, lga_id),
        
house AS
		(select state_id,state_name,house_id,house_code,house_name, sum(A) AS A, sum(AA) AS AA, sum(AAC) AS AAC, 
			sum(ADC) AS ADC, sum(ADP) AS ADP, sum(APC) AS APC, sum(APGA) AS APGA,
			sum(APM) AS APM, sum(APP) AS APP, sum(BP) AS BP, sum(LP) AS LP,
			sum(NRM) AS NRM, sum(NNPP) as NNPP, sum(PDP) AS PDP, sum(PRP) AS PRP, 
			sum(SDP) AS SDP, sum(YPP) AS YPP, sum(ZLP) AS ZLP, 
			sum(Total_Rejected_votes) AS Total_Rejected_votes, sum(Total_Registered_voters) AS Total_Registered_voters,
			sum(Total_Accredited_voters) AS Total_Accredited_voters,

			(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
          	sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)) AS total_valid_votes,

          (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
           sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))
          AS total_vote_casted, 
		
 		 IF (((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) > Total_Accredited_voters) ,
            (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) - sum(Total_Accredited_voters),
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            sum(Total_Accredited_voters) - sum(Total_Registered_voters), 0)
                 ) AS over_vote_values,
                 
		IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) and 
            sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
         IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) ,
            'Over Votting! Because total votes casted are greater than total accredited voters',  
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
           'Over Votting! Because total accredited voters are greater than total registered voters', 
        IF(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)>0,'OK','non collated')
                   ))) AS remarks, 
             
 		IF (sum(Total_Registered_voters)>0 and
           sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)>0,             
           CONCAT(ROUND((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))/sum(Total_Registered_voters) *100,2),'%'), 
       IF (sum(Total_Registered_voters)<=0,'Warning!! total registered voters = 0','not collated')) 
       AS percentage_voters_turnout        
       FROM lgat GROUP BY house_id),
        

win_w AS
         (SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM wt 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM wt 
          UNION
       	  SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM wt  
          UNION
		  SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM wt   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM wt  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM wt   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM wt   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM wt 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM wt 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, ward_id, state_name,lga_name,ward_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM wt  ),

win_l AS
         (SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM lgat  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM lgat   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM lgat  ),
          
win_h AS
         (SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM house   
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM house   ),
          
 
  win_ward AS
           (SELECT state_id,house_id,house_code,house_name, lga_id, ward_id,state_name,lga_name, ward_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY ward_name ORDER BY votes DESC) AS row_num FROM win_w),
                
win_lga AS
           (SELECT state_id,house_id,house_code,house_name, lga_id,state_name,lga_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY lga_name ORDER BY votes DESC) AS row_num FROM win_l),
                
win_house AS
           (SELECT state_id,house_id,house_code,house_name,state_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY house_id ORDER BY votes DESC) AS row_num FROM win_h),

non_collated_ward AS 
			(SELECT distinct ward_id,state_id,house_id,house_code,house_name,lga_id,state_name,lga_name, ward_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id, ward_id) AS Total_Registered_voters,
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id, ward_id) AS total FROM wt),   -- 7. non collated wards
			
non_collated_lga AS 
			(SELECT DISTINCT  lga_id, state_id,house_id,house_code,house_name,state_name,lga_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM wt),

non_collated_house AS 
			(SELECT DISTINCT state_id,house_id,house_code,house_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters, 
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM wt),		
		
collated_ward AS 
			(SELECT distinct ward_id,state_id,house_id,house_code,house_name,lga_id,state_name,lga_name, ward_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id, ward_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id, ward_id) AS total FROM wt),

collated_lga AS
			(SELECT distinct lga_id,state_id,house_id,house_code,house_name,state_name,lga_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM wt),

collated_house AS
			(SELECT distinct state_id,house_id,house_code,house_name,state_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM wt)   


   """

}

presidential_table_lga ={
	
	"query": f"""

WITH lgat AS

    (SELECT *, (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP) AS total_valid_votes,

          (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes)
          AS total_vote_casted, 
          
          IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
              YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
              (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
               Total_Rejected_votes) - Total_Accredited_voters,
               IF( Total_Accredited_voters  > Total_Registered_voters,
               Total_Accredited_voters - Total_Registered_voters, 0)
                 ) AS over_vote_values,

         IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters and 
                   Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
          	    IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
                   'Over Votting! Because total votes casted are greater than total accredited voters',  
                   IF( Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total accredited voters are greater than total registered voters', 
                   IF (status='canceled','canceled',
                   IF(A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP>0,'OK','non collated')
                   )))) AS remarks,
                 
             IF (status='canceled','canceled',
             IF (Total_Registered_voters>0 and
            	 A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes>0,             
                 CONCAT(ROUND((A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
                 Total_Rejected_votes)/Total_Registered_voters *100,2),'%'), 
                 if (Total_Registered_voters<=0,'Warning!! total registered voters = 0','not collated')) 
                 
                 ) AS percentage_voters_turnout


            FROM house_lga_table),


house AS
		(select state_id,state_name,house_id,house_code,house_name, sum(A) AS A, sum(AA) AS AA, sum(AAC) AS AAC, 
			sum(ADC) AS ADC, sum(ADP) AS ADP, sum(APC) AS APC, sum(APGA) AS APGA,
			sum(APM) AS APM, sum(APP) AS APP, sum(BP) AS BP, sum(LP) AS LP,
			sum(NRM) AS NRM, sum(NNPP) as NNPP, sum(PDP) AS PDP, sum(PRP) AS PRP, 
			sum(SDP) AS SDP, sum(YPP) AS YPP, sum(ZLP) AS ZLP, 
			sum(Total_Rejected_votes) AS Total_Rejected_votes, sum(Total_Registered_voters) AS Total_Registered_voters,
			sum(Total_Accredited_voters) AS Total_Accredited_voters,

			(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
          	sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)) AS total_valid_votes,

          (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
           sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))
          AS total_vote_casted, 
		
 		 IF (((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) > Total_Accredited_voters) ,
            (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)) - sum(Total_Accredited_voters),
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            sum(Total_Accredited_voters) - sum(Total_Registered_voters), 0)
                 ) AS over_vote_values,
                 
		IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) and 
            sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
            'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
         IF (sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes) > sum(Total_Accredited_voters) ,
            'Over Votting! Because total votes casted are greater than total accredited voters',  
        IF( sum(Total_Accredited_voters)  > sum(Total_Registered_voters),
           'Over Votting! Because total accredited voters are greater than total registered voters', 
        IF(sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
            sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
			sum(SDP)+ sum(YPP) +sum(ZLP)>0,'OK','non collated')
                   ))) AS remarks, 
             
 		IF (sum(Total_Registered_voters)>0 and
           sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes)>0,             
           CONCAT(ROUND((sum(A) + sum(AA) +sum(AAC) + sum(ADC)+ sum(ADP) + sum(APC) + sum(APGA)+sum(APM)+ 
           sum(APP)+ sum(BP)+ sum(LP) +sum(NRM) +sum(NNPP)+ sum(PDP)+sum(PRP) +
		   sum(SDP)+ sum(YPP) +sum(ZLP) +sum(Total_Rejected_votes))/sum(Total_Registered_voters) *100,2),'%'), 
       IF (sum(Total_Registered_voters)<=0,'Warning!! total registered voters = 0','not collated')) 
       AS percentage_voters_turnout        
       FROM house_lga_table GROUP BY house_id),
        

win_l AS
         (SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM lgat  
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM lgat 
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM lgat   
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM lgat
          UNION
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM lgat 
          UNION 
          SELECT state_id,house_id,house_code,house_name, lga_id, state_name,lga_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM lgat  ),
          
win_h AS
         (SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM house   
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM house   ),
          
  
win_lga AS
           (SELECT state_id,house_id,house_code,house_name, lga_id,state_name,lga_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY lga_name ORDER BY votes DESC) AS row_num FROM win_l),
                
win_house AS
           (SELECT state_id,house_id,house_code,house_name,state_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY house_id ORDER BY votes DESC) AS row_num FROM win_h),

non_collated_lga AS 
			(SELECT DISTINCT  lga_id, state_id,house_id,house_code,house_name,state_name,lga_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM wt),

non_collated_house AS 
			(SELECT DISTINCT state_id,house_id,house_code,house_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters, 
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM wt),		

collated_lga AS
			(SELECT distinct lga_id,state_id,house_id,house_code,house_name,state_name,lga_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM wt),

collated_house AS
			(SELECT distinct state_id,house_id,house_code,house_name,state_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM wt)

	"""
	
}

presidential_table_state ={
	
	"query": f"""

WITH house AS

    (SELECT *, (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP) AS total_valid_votes,

          (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes)
          AS total_vote_casted, 
          
          IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
              YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
              (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
               Total_Rejected_votes) - Total_Accredited_voters,
               IF( Total_Accredited_voters  > Total_Registered_voters,
               Total_Accredited_voters - Total_Registered_voters, 0)
                 ) AS over_vote_values,

         IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters and 
                   Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total votes casted are greater than total accredited voters and also total accredited voters are greater than total registered voters', 
          			IF (A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + 
                   YPP + ZLP + Total_Rejected_votes > Total_Accredited_voters ,
                   'Over Votting! Because total votes casted are greater than total accredited voters',  
                   IF( Total_Accredited_voters  > Total_Registered_voters,
                   'Over Votting! Because total accredited voters are greater than total registered voters', 
                   IF((A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP) != total_valid_votes_c,'Error!! Recorded Total Valid Votes is not correct',
                   IF (status='canceled','canceled',
                   IF (status='non collated','non collated',
                   IF(A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP>0,'OK','check manually, please..')
                   )))))) AS remarks,                      
                 
                 
             IF (status='canceled','canceled',
             IF (Total_Registered_voters>0 and
            	 A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP + Total_Rejected_votes>0,             
                 CONCAT(ROUND((A + AA + ADP + APP + AAC + ADC + APC + APGA + APM + BP + LP + NRM + NNPP + PDP + PRP + SDP + YPP + ZLP +
                 Total_Rejected_votes)/Total_Registered_voters *100,2),'%'), 
                 if (Total_Registered_voters<=0,'Warning!! total registered voters = 0','Warning!! validate the result')) 
                 
                 ) AS percentage_voters_turnout


            FROM house_table),   
  
win_h AS
         (SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, A AS votes, "A" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AA AS votes, "AA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADP AS votes, "ADP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APP AS votes, "APP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, AAC AS votes, "AAC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ADC AS votes, "ADC" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APC AS votes, "APC" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APGA AS votes, "APGA" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, APM AS votes, "APM" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, BP AS votes, "BP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, LP AS votes, "LP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NRM AS votes, "NRM" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, NNPP AS votes, "NNPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PDP AS votes, "PDP" AS party FROM house   
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, PRP AS votes, "PRP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, SDP AS votes, "SDP" AS party FROM house 
          UNION
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, YPP AS votes, "YPP" AS party FROM house 
          UNION 
          SELECT state_id,house_id,house_code,house_name, state_name, Total_Registered_voters,total_vote_casted,Total_Accredited_voters,over_vote_values,remarks,total_valid_votes, ZLP AS votes, "ZLP" AS party FROM house   ),
  
win_house AS
           (SELECT state_id,house_id,house_code,house_name,state_name, votes, Total_Registered_voters,Total_Accredited_voters,
           		total_vote_casted,total_valid_votes,
                IF (total_vote_casted>0,CONCAT(ROUND(votes/total_vote_casted*100,2),'%'),'Collation has not started') AS 
                percentage_votes,party,ROW_NUMBER() OVER(PARTITION BY house_id ORDER BY votes DESC) AS row_num FROM win_h),

non_collated_lga AS 
			(SELECT DISTINCT  lga_id, state_id,house_id,house_code,house_name,state_name,lga_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id,lga_id) AS Total_Registered_voters,
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id,lga_id) AS total FROM wt),

non_collated_house AS 
			(SELECT DISTINCT state_id,house_id,house_code,house_name,sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters, 
			sum(case when status = 'non collated' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM wt),		

collated_house AS
			(SELECT distinct state_id,house_id,house_code,house_name,state_name, sum(Total_Registered_voters) OVER(PARTITION BY state_id) AS Total_Registered_voters,
			sum(case when status = 'collated' OR status = 'canceled' then 1 else  0 end) OVER(PARTITION BY house_id) AS total FROM wt)         


	"""
	
}