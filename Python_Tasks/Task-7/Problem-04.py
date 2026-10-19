# 4.Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):

    reversed_string = s[::-1]

    string_ascii_ferqi = []
    reversed_string_ascii_ferqi = []

    for i in range(1, len(s)):
        string_ascii_ferqi.append(abs(ord(s[i]) - ord(s[i - 1])))

    for i in range(1, len(reversed_string)):
        reversed_string_ascii_ferqi.append(abs(ord(reversed_string[i]) - ord(reversed_string[i - 1])))

    if string_ascii_ferqi == reversed_string_ascii_ferqi:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
