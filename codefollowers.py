import twint

c = twint.Config()
a= input("Enter username: ")
c.Username = a
c.Store_csv = True
c.Output = "sumitfollowers.csv"  
print("Your Followers are as follows : ")
twint.run.Followers(c)
