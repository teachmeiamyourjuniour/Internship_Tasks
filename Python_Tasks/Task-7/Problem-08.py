# 8.Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def gemstones(arr):
    # Write your code here
    ls = list(set(arr[0]))
    sm = len(ls)
    for x in ls:
        for i in range(1,len(arr)):
            if x not in arr[i]:
               sm -=1
               break
    return sm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
