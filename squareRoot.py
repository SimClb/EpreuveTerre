import sys 

print("\n################################################################## \n"
      "########################### SQUARE ROOTER ######################### \n"
      "################################################################## \n")

if len(sys.argv) > 2 or len(sys.argv) <= 1:
    print("Veuillez entrer un nombre en arguments")
    exit()

number = sys.argv[1]

try: 
    isInt = int(number)
    if isInt < 0:
        print("Vous devez mettre un entier positif en arguement")
        exit()
except ValueError:
    print("Vous devez mettre un entier en argument")
    exit()

# print our sqare root
print(int(9**0.5))

#finished
