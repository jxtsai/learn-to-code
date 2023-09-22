import re

pattern = "@"

email = "jxtsai@duck.com"
if re.search(pattern, email, flags=0):
# syntax re.serach(pattern, string, flags = 0)
#     
    print("Valid")
else:
    print("invalid")    