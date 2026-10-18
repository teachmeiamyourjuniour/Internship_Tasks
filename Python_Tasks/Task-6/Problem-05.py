# 5.Write a Function
# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    if year > 1800:
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
        elif year%4==0:
            leap=True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))
