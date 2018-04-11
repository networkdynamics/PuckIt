Xs = ["Year_Founded","Year_Joined_NHL","Franchise_Moved__Kind_of_invalid","Stadium_Capacity","VAR6","Number_of_Stanley_Cup_Wins","Last_Time_Won_Stanley_Cup","Number_of_Stanley_Cup_Finals_App","Most_Recent_Stanley_Cup_Finals_A","Last_Time_Made_Playoffs__Does_no","Number_of_Playoff_Appearances_ov","sum_playoff_lengths_5_years","Total_Number_of_Playoff_Appearan","Average_Secondary_Market_Ticket","Team_Net_Worth__Again__unsure_of","Team_Debt_Value","Team_Revenue__Again__unsure_of_c","Team_Operating_Income__Again__un","Same_State_Teams","Population","Median_Household_Income","Latitude"]

Ys = ["Subscribers","Moderators","Number_of_Comments","Median_number_of_comments_per_us","Number_of_users","Number_of_posts","clustering","assortativity","pearson_corr_coef","clique_size","number_of_cliques","transitivity","number_weak_comp"]



for x in Xs:
    for y in Ys:
        print 'proc sgplot data=WORK.IMPORT; scatter x= %s y= %s / datalabel=Team datalabelattrs=(size=10);xaxis grid;yaxis grid;run;' % (x, y)
