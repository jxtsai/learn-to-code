'''
Write a simple regex to validate a username. Allowed characters are:

    lowercase letters,
    numbers,
    underscore

Length should be between 4 and 16 characters (both included).


'''

import re

def validate_usr(username):
    #your code here
    
    m = re.match(r"[^A-Z]+[a-z0-9_]+", username, flags = 0)
    
    print(m) 
    if len(username) < 4 or len(username) > 16:
        return False
    else:
        if re.match(r"[^A-Z]+[a-z0-9_]+", username, flags = 0):
            return True
        else:
            return False
            

test = validate_usr('Hass')
print(test)