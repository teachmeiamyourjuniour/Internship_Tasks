# 16.Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
sizes = Counter(list(map(int, input().split())))
N = int(input())
total = 0
for i in range(N):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        sizes[size] -= 1
        total += price
print(total)
