# 14.Anagram
# https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    n = len(s)
    
    # If the length is odd, it's impossible to split equally
    if n % 2 != 0:
        return -1
        
    # Split the string into two equal halves
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Count character frequencies for both halves
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Calculate how many characters from s1 are missing in s2
    # The '-' operator on Counters calculates (count1[char] - count2[char]) 
    # and keeps only positive differences.
    diff = count1 - count2
    
    # The sum of these values gives the total changes needed
    return sum(diff.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
