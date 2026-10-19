# 12.Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem

#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

def makingAnagrams(s1, s2):
    # Count character frequencies for both strings
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Get all unique characters present across both strings
    all_chars = set(count1.keys()).union(set(count2.keys()))
    
    # Calculate total deletions needed
    deletions = 0
    for char in all_chars:
        deletions += abs(count1[char] - count2[char])
        
    return deletions
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
