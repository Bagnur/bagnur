#Detect Floating Point Number

import re

x=int(input())
for i in range(0,x):
    y=input()
    if (re.search('^[+-\.]\d+\.\d+',y)):
        print('True')
    else: print("False")
