import os,sys
import checker
import json

username = sys.argv[1]
# username = input()
account = checker.check(username)
json_string = json.dumps(account)
print(json_string)

try:
    os.chdir(os.getcwd()+'/Python_Scripts/result/')
except:
    pass

with open("userpresent.json","w") as f:
    json.dump(account,f, indent=4)
