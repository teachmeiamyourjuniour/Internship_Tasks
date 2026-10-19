# 3.Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    i = 0
    count = 0
    while i < len(s):
        if(s[i]!="S"):
            count = count + 1
        if(s[i+1] != "O"):
            count = count + 1
        if(s[i+2] != "S"):
            count = count + 1
        i = i + 3
    return count 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
