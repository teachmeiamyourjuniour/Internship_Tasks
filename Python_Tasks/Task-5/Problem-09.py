# 9.Word Order
# https://www.hackerrank.com/challenges/word-order/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k=[]
for i in range(n):
    g=input()
    k.append(g)
h=set(k)
l={}
for i in k:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
hh=sorted(l)
print(len(h))
print(*l.values())
