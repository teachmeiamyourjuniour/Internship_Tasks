# 6.Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def pangrams(s):
    lo = s.lower()
    count = []
    sl = ["a","b","c","d","e","f","g","h","i","j","k","l",
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i in lo:
        if i in sl:
            count.append(i)

    n = set(count)
    print(n)

    if len(n) == 26:
        return('pangram')
    else:
        return('not pangram')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
