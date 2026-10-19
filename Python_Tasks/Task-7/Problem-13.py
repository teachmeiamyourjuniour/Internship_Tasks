# 13.Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # 1. Count the frequency of each character
    char_counts = Counter(s)
    
    # 2. Count the frequency of those frequencies
    freq_counts = Counter(char_counts.values())
    
    # If all characters already appear the exact same number of times
    if len(freq_counts) == 1:
        return "YES"
        
    # If there are more than 2 distinct frequencies, it's impossible to fix with 1 removal
    if len(freq_counts) > 2:
        return "NO"
        
    # If there are exactly 2 distinct frequencies, unpack them
    (f1, count1), (f2, count2) = freq_counts.items()
    
    # Case 1: One frequency occurs exactly once, and it is a count of 1.
    # e.g., "aabbcccd" -> frequencies are {2:3, 1:1}. Removing 'd' makes it valid.
    if (f1 == 1 and count1 == 1) or (f2 == 1 and count2 == 1):
        return "YES"
        
    # Case 2: One frequency is exactly 1 greater than the other, and it only happens once.
    # e.g., "aabbccc" -> frequencies are {2:2, 3:1}. Removing one 'c' yields 2.
    if (f1 - f2 == 1 and count1 == 1) or (f2 - f1 == 1 and count2 == 1):
        return "YES"
        
    # Any other combination is invalid
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
