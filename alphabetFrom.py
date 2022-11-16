# faire un programme qui affiche l'alphabet en lettre minuscules suivi d'un retour à la ligne
import sys

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

isNumber = sys.argv[1].isnumeric()

if isNumber:
    print("Veuillez rentrer une lettre et non un chiffre en argument...")
    exit()
elif len(sys.argv[1]) > 1:
    print("Veuillez n'entrer qu'une seule lettre en argument...")
    exit()


#fromIndex = letters.index(str(sys.argv))
#print("Voici l'alphbat à partir de la lettre que vous avez demandé: \n", letters[fromIndex:])
