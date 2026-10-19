# 1.Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to 
aa=int(input())
a=set(map(int,input().split()))
bb=int(input())
b=set(map(int,input().split()))

x=a^b
s=0
for _ in x:
    s+=1
print(s)
