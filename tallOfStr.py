import sys 

# we don't want int, we want just one arguments,  
if len(sys.argv) > 2 or len(sys.argv) <= 1:
    print("Veuillez entrez un argument...")
    exit()

argument = str(sys.argv[1])

# check if arg is a number
isNumber = argument.isnumeric

if isNumber:
    print("N'entrez qu'une str en argument...")
    exit()

print(len(argument))

#finished 