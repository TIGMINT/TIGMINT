import twint


#configuration
con = twint.Config()
Recentword = input("Enter Word to scrap the tweet -: ")
con.Search = Recentword
con.Lang = "en"  #configure the language 
#Putting the limit
limitt = input("Enter the limit -: ")
con.Limit = limitt
#For Date input
Sdatee = input("Enter the Starting Date in given format ~ YYYY-MM-DD :") #Starting Date 
con.Since = Sdatee
Edatee = input("Enter the Starting Date in given format ~ YYYY-MM-DD :") #End Date 
con.Until = Edatee
con.Store_csv = True
con.Output = "Recentword.csv"
twint.run.Search(con)
