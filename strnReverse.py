# we have to reverse of the arguments 
import sys 
import re

#check if is there one argument
if len(sys.argv) <= 1:
    print("Veuillez entrer au moins un argument")
    exit()

#creat a list of our argu
list = sys.argv
newList = ""

#add to a var 
for n in list[1:]:
    print(n)
    newList += (n + " ")

#replace wrong chars 
for wrongChar in newList:
    if wrongChar in '"':
        newList.replace(wrongChar, '')

#create new var reversed with var from our list into
strReverse = newList[::-1]
#replace the first space 

#use regex to remove the first whitespace


