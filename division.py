# print the result and the rest of a division from deux arguments 
import sys


if len(sys.argv) > 3 or len(sys.argv) <= 1:
    print("Veuillez entrer deux nombres en arguments")
    exit()

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
msg = 'erreur.'

if number1 < number2:
    print(msg)
    exit()
elif number2 == 0:
    print(msg)
    exit()
else:
    print("resultat: ", int(number1/number2), "\n reste: ", int(number1 % number2))

#finished