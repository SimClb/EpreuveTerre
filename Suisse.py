import sys 

if len(sys.argv) != 4:
    print("Veuillez entrer trois nombres en arguments")
    exit()

for n in sys.argv[1:]:
    isNumber = n.isnumeric()
    if isNumber == False:
        print("Veuillez n'entrer que des entiers....")
        exit()


list = sys.argv[1:]
number = list.index(max(list)) + list.index(min(list))

if number == 3:
    print(list[0])
elif number == 2:
    print(list[1])
elif number == 1:
    print(list[2])


#finished 