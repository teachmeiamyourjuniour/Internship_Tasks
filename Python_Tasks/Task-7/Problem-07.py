# 7.Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    # your code goes here
    letter = string.ascii_lowercase[0:size][::-1]
    for i in [size - abs(j) for j in range(-size+1, size)]:
        print('-'.join(letter[0:i]+letter[0:i-1][::-1]).center(4*size - 3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
