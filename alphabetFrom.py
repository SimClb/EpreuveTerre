# faire un programme qui affiche l'alphabet en lettre minuscules suivi d'un retour à la ligne
import sys

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#if argument is a number ==> bools true 
isNumber = sys.argv[1].isnumeric()


#check if argument is ok 
if isNumber:
    print("Veuillez rentrer une lettre et non un chiffre en argument...")
    exit()
elif len(sys.argv[1]) > 1:
    print("Veuillez n'entrer qu'une seule lettre en argument...")
    exit()

#take the index of the argument 
fromIndex = letters.index(str(sys.argv[1]))
newList = letters[fromIndex:]
listToPrint = ""

for letter in newList:
    listToPrint += letter

print(listToPrint)

#finished 