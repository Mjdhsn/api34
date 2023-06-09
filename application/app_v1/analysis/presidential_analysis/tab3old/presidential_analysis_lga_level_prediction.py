from application.app_v1.database import get_db
from application.app_v1.analysis.presidential_analysis.tab3.party_table import lga_query

import json



table_list = ["total_over_voting_table"]

where_list = ["over_voting","total_over_voting","total_over_voting_table"]

# QUERIES
conditions_lga = {
       "total_registered_voters": f"""{lga_query['query']} SELECT  COALESCE(sum(Total_Registered_voters),0) as count1 from lgat""",
       "total_accredited_voters": f"""{lga_query['query']}  SELECT  COALESCE(sum(Total_Accredited_voters),0) as count1 from lgat""",
       "total_rejected_votes": f"""{lga_query['query']}  SELECT  COALESCE(sum(Total_Rejected_votes),0) as count1 from lgat """,
       "total_valid_votes": f"""{lga_query['query']}  SELECT  COALESCE(sum(total_valid_votes),0) as count1  from lgat """,
        "total_vote_casted": f"""{lga_query['query']}  SELECT  COALESCE(sum(total_vote_casted),0) as count1 from lgat""",
        # "percentage_voters_turnout": f"""{lga_query['query']}  SELECT percentage_voters_turnout as count1  from lgat""",
       "over_voting": f"""{lga_query['query']}  SELECT count(*) as count1  from lgat where over_vote_values>0""",
       "total_over_voting": f"""{lga_query['query']}  select COALESCE(sum(over_vote_values),0) as count1 from lgat where over_vote_values>0""",
        "total_over_voting_table":f"""{lga_query['query']}  SELECT state_name,lga_name,over_vote_values,remarks,percentage_voters_turnout,Total_Registered_voters  from lgat where over_vote_values>0""",
       "message": f"""{lga_query['query']} 

	SELECT CASE 			

	WHEN  ((select diff from exp_winner limit 1,1)  < 
			(select COALESCE(sum(Total_Registered_voters),0) from lgat where (status='canceled' or status='non collated'))) 
			and  ((select count(*) from lgat where (status='canceled' or status='collated')) != (select count(*) from lgat))
		THEN ('Collation In PROGRESS!! Please Visit Again Later.') 
		
	WHEN ( ((select diff from exp_winner limit 1,1) > 
			(select COALESCE( sum(Total_Registered_voters),0) from lgat where status='canceled')) and (select count1>=37/3*2 from exp_winner limit 1 ))
   	    THEN (concat((select party from exp_winner limit 1),'Predicted to be WINNER!! of the 2023 Nigerian Presidential Election')) -- predicted winner
   	    
	WHEN ( ((select diff from exp_winner limit 1,1) > 
			(select COALESCE ( sum(Total_Registered_voters),0) from lgat where status='canceled')) and (select count1<37/3*2 from exp_winner limit 1 ))
   		 THEN ("The 2023 Nigerian Presidential Election PREDICTED to be INCONCLUSIVE!! because, the leading party didn't got one-quarter of votes casted at the presidential election in each of at least two-thirds of all States in the Federation and the FCT, Abuja.") 
		
    WHEN ( ((select diff from exp_winner limit 1,1) <= 
			(select COALESCE ( sum(Total_Registered_voters),0) from lgat where status='canceled')) and (select count1>=37/3*2 from exp_winner limit 1 )
			and  ((select count(*) from lgat where (status='canceled' or status='collated')) = (select count(*) from lgat)))
    	THEN ('The 2023 Nigerian Presidential Election PREDICTED to be INCONCLUSIVE!! because the margin between the two leading candidates is not in excess of the total number of registered voters of the
			Polling Unit(s) where the election was cancelled or not held')
    
    ELSE 'Please Visit Again Later'
END as messages

	 """,

       "party_table": f"""{lga_query['query']}
        
        SELECT ROW_NUMBER() OVER(PARTITION BY country_name ORDER BY votes DESC) AS row_num,party,votes as Scores,		-- 11
       concat(round(votes/total_vote_casted*100,2),'%') as percentage_score FROM win_country  	
       
       
         """
}



# lga results

def get_lga_lga_all_results():
    with get_db() as conn:
        cur = conn.cursor()
     
        final_results = {}

        key_values = []
        execute_queries = []
        for key, val in conditions_lga.items():
            execute_queries.append(val)
            key_values.append(key)
        
        map1 = ['state_name','lga_name']
        map2 = ['Total_Registered_voters','Total_Accredited_voters','Total_Rejected_votes']
        map3 = ['remarks']
        map4 =['over_vote_values','percentage_voters_turnout','Total_Registered_voters']
            
        try:

            for index, val in enumerate(execute_queries):

                name_val = []
                total_val = []
                other_val = []
                
                try:

                    cur.execute(val)
                    val_results = cur.fetchall()
                except:
                    print("error")

                if key_values[index] in table_list:
                        res = {}

                        if val_results:
                            for val in val_results:
                                filterByKey = lambda keys: {x: val[x] for x in keys}
                                names = filterByKey(map1)
                                total =  filterByKey(map4)
                                other =  filterByKey(map3)
                                name_val.append(names)
                                total_val.append(total)
                                other_val.append(other)

                            res['names'] = name_val
                            res['total'] = total_val
                            res['other'] = other_val
                            val = [res]
                            final_results[key_values[index]] = val

                        else:
                            res['names'] = {}
                            res['total'] = {}
                            res['other'] = {}
                            val = [res]
                            final_results[key_values[index]] = val
                else:
                        final_results[key_values[index]] = val_results
            
            return final_results
        except Exception as e:
            print(e)
            return str(e)