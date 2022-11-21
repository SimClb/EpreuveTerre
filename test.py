import sys
#string = "aa"
#
#print(sys.argv)

import hashTableTime

# function to return key for any value

#val = parametre of function 
# creation of variable key and value 

def get_key(val):
    for key, value in hashTableTime.changeHour.items():
        if val == value:
            return key

    return "key doesn't exist"

print(get_key("3"))

