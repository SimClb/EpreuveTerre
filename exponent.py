import sys 

print("\n################################################################## \n"
      "######################### EXPONENT PRINTER ####################### \n"
      "################################################################## \n")

if len(sys.argv) > 3 or len(sys.argv) <= 1:
    print("Veuillez entrer deux nombres en arguments")
    exit()

listArgv = sys.argv 

for n in listArgv[1:]:
    isNumber = n.isnumeric()
    if isNumber == False:
        print(n, "n'est pas un nombre ! (si float avec ',' mettre avec '.'")
        exit()

print(int(sys.argv[1]) ** int(sys.argv[2]))

#finished