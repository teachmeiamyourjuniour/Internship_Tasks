# 16.Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = []
    
 
    for char in s:
  
        if 'A' <= char <= 'Z':
        
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)
 
        elif 'a' <= char <= 'z':
       
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)
        else:
        
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
