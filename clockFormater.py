import sys 
import hashTableTime

#this script is for ex 14 and 15 so he's running for 24 to 12 and 12 to 24

errorMsg = "Veuillez entrer une heure valide..."

#functions: 

def get_key(valEnter):
    # var key and value for hashtable in items()
    for key, value in hashTableTime.changeHour.items():
        if valEnter == value:
            return key

    return "Key doesn't exist"


print("#################################################### \n"
      "################ 24To12 vise versa ################# \n"
      "#################################################### \n"
    )

if len(sys.argv) > 2 or len(sys.argv) <= 1:
    print("Veuillez n'entrer qu'un seul argument")
    exit()

hour = sys.argv[1]

#let's check if it's an hour or not...
hours = hour[:2]
symbol = hour[2:3]
minutes = hour[3:5]

isNumberHour = hours.isnumeric()
isNumberMinutes = minutes.isnumeric()

if isNumberHour and isNumberMinutes and symbol == ":":
    pass
else:
    print(errorMsg, 1)
    exit()

# 12h : 1, 24h : 2
format = 0
# let's check if 12h or 24h format...

if len(hour) == 5:
    format += 2

elif len(hour) == 7:
    format += 1

    if int(hours) > 12:
        print(errorMsg, 2)
        exit()
    elif hour[5:7].upper() == "PM" or hour[5:7].upper() == "AM":
        pass
    else:
        print(errorMsg, 3)
        exit()

elif len(hour) != 5 and len(hour) != 7:
    print(errorMsg, 4)
    exit()

#format 24h -> 12
if format == 2:
    if int(hours) < 12 and int(hours) != 00:
        print(hour + "AM")
    if int(hours) == 12:
        print(hour + "PM")
    elif int(hours) == 00 or int(hours) == 24:
        print("12"+ hour[2:5] + "AM")
    elif int(hours) > 12:
        print(hashTableTime.changeHour[hours] + hour[2:5] + "PM")
        
#format 12h -> 24
elif format == 1: 
    if int(hours) < 12 and hour[5:7].upper() == "AM":
        print(hour[:5])
    elif int(hours) == 12 and hour[5:7].upper() == "PM":
        print(hour[:5])
    elif int(hours) == 12 and hour[5:7].upper() == "AM":
        print("00" + hour[2:5])
    elif hour[5:7].upper() == "PM":
        print(get_key(hours) + hour[2:5])


#finished 


