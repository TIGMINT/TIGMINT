import twint

c = twint.Config()
a= input("Enter username: ")
c.Username = a
c.Store_csv = True
c.Output = "sumitbio.csv"
print("Your BIO is as follows : ")
twint.run.Lookup(c)
