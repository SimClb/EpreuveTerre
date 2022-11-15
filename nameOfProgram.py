# create a program who show you the name of file 
import sys
import os 

#take the path of __file__ (current file) and take the basename 
print(os.path.basename(__file__))


# second method 
#print the first arguments so the file name 
print(sys.argv[0])

#finished