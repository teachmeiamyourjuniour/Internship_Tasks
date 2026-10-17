# 8.Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
kk=[]
for i in range(n):
    k=input()
    kk.append(k)
x=set(kk)
print(len(x))
