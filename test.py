import sys
#string = "aa"
#
#print(sys.argv)

list = [34, 28, 32]

number = list.index(max(list)) + list.index(min(list))

if number == 3:
    print(list[0])
elif number == 2:
    print(list[1])
elif number == 1:
    print(list[2])