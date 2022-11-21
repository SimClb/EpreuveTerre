import sys 

if len(sys.argv) <=1:
    print("veuillez rentrer au moins un chiffre...")
    exit()

numbers = []

for number in sys.argv[1:]:
    isNumber = number.isnumeric()
    if isNumber == False:
        print("erreur.")
        exit()
    else:
        numbers.append(int(number))
        


#boucle for chaque boucle il vérif si le n-1 était plus petit si non print('pas triée')

sorted = 0
notSorted = 0

for n in numbers[1:]:
    index = numbers.index(n)
    if n > numbers[index - 1]:
        sorted += 1
    else:
        notSorted += 1


if notSorted != 0:
    print("Pas triée !")
else: 
    print("Triée !")

#finished 