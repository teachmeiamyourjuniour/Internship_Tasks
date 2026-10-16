# 14.Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

n=int(input())
kk=[]
for i in range(n):
    k=input()
    kk.append(k)
x=set(kk)
print(len(x))
