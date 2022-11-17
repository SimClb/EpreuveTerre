import sys
#string = "aa"
#
#print(sys.argv)

import re

string = " test ma gueule"
result = re.sub(r'^\s', '', string)
print(result)