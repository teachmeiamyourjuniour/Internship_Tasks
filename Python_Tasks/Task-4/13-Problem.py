# 13.Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
nn=set(map(int,input().split(" ")))
m=int(input())
mm=set(map(int,input().split(" ")))
c=sorted(nn.difference(mm).union(mm.difference(nn)))

for i in c:
    print(i)
