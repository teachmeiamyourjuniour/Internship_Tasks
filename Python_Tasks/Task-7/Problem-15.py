# 15.Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



def gameOfThrones(s):

    counts = Counter(s)
    

    odd_counts = 0
    for frequency in counts.values():
        if frequency % 2 != 0:
            odd_counts += 1
            

    if odd_counts <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
