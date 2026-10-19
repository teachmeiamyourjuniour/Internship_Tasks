# 17.Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbe#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys


def separateNumbers(s):
    n = len(s)
  
    if n < 2:
        print("NO")
        return

    for i in range(1, (n // 2) + 1):
        first_sub = s[:i]
        
        if first_sub[0] == '0' and len(first_sub) > 1:
            break
            
        first_num = int(first_sub)
        
        valid_sequence = ""
        current_num = first_num
        
        while len(valid_sequence) < n:
            valid_sequence += str(current_num)
            current_num += 1
            
        if valid_sequence == s:
            print(f"YES {first_num}")
            return
            
    print("NO")
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
