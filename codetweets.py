import twint

c = twint.Config()
a= input("Enter username: ")
c.Username = a

c.Store_csv = True
c.Output = "sumittweets.csv"  
twint.run.Search(c)
