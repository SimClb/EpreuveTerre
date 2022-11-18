#print if a number is prime or not 
import sys

print("############################################ \n"
     "############## PRIME NUMBER ################ \n"
     "############################################ \n")

if len(sys.argv) > 2 or len(sys.argv) <= 1:
    print("Mets deux chiffres")
    exit()

isNumber = sys.argv[1].isnumeric()
if isNumber == False:
    print("pas d'str stp que des int")
    exit()


checkerNumber = 0

for n in range(1, 10):
    calcule = int(sys.argv[1]) % int(n)
    if calcule != 0:
        continue
    elif calcule == 0:
        checkerNumber += 1

if checkerNumber == 2:
    print(f"Oui, {sys.argv[1]} est un nombre premier")
else:
    print(f"Non, {sys.argv[1]} n'est pas un nombre premier")

#finished