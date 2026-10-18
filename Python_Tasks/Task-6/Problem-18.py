# 18.Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

len_a = int(input())
set_a = set(input().split())
for _ in range(0, int(input())):
    cmd = input().split()[0]
    getattr(set_a, cmd)(set(input().split()))
print(sum(map(int,set_a)))
