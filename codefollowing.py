import twint

c = twint.Config()
a= input("Enter username: ")
c.Username = a
c.Store_csv = True
c.Output = "sumitfollowing.csv"
print("Your Folowings are as below : ")
twint.run.Following(c)
