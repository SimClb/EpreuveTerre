#if it's a even number 
import sys 

#check if the user put an argument 
if len(sys.argv) > 2 or len(sys.argv) <= 1:
    print("Tu ne me la mettras pas à l'envers")
    exit()

argument = sys.argv[1]
isNumber = argument.isnumeric()

#check if is an even numer or not 
if isNumber:
    if int(argument) % 2 == 0:
        print("Pair")
    else:
        print("Impair")
else:
    print("Tu ne me la mettras pas à l'envers.")

#finished 