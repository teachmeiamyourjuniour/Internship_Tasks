# 19.Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def weightedUniformStrings(s, queries):

    valid_weights = set()
    
    current_weight = 0
    prev_char = ""
    

    for char in s:
       
        weight = ord(char) - ord('a') + 1
 
        if char == prev_char:
            current_weight += weight
        else:
            current_weight = weight
            prev_char = char
            
        valid_weights.add(current_weight)

    result = []
    for q in queries:
        if q in valid_weights:
            result.append("Yes")
        else:
            result.append("No")
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
