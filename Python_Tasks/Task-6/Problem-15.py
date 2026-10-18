# 15 Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

e, a = int(input()), set(map(int, input().split()))
f, b = int(input()), set(map(int, input().split()))

print(len(a - b))
