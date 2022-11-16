import sys
#string = "aa"
#
#print(sys.argv)

list = sys.argv
newList = ""
for n in list[1:]:
    print(n)
    newList += (n + " ")

print(newList)
