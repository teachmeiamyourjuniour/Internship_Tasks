# 14 Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

e, a = int(input()), set(map(int, input().split()))
f, b = int(input()), set(map(int, input().split()))

print(len(a & b))
