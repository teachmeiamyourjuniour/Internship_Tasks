# 16.Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

t= int(input())
for i in range(t):
    a= int(input())
    setA = set(map(int,input().strip().split``()))
    b = int(input())
    setB = set(map(int,input().strip().split()))
    if setA.issubset(setB):
        print(True)
    else:
        print(False)
