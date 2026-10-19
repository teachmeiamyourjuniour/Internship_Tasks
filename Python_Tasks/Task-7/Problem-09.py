# 9.Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    cpt=0
    a = 'using a to stock the first index of "010" when found it'
    while True:
        a = b.find('010')
        if a==-1 : 
            break
        up = '1' if b[a+2] == '1' else '1'
        b = b[:a+2] + up + b[a+3:] 
        cpt+=1
    return cpt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
