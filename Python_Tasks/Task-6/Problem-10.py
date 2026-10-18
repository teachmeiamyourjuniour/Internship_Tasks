# 10.Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem

n , m = map(int, input().split())

j=1
lines_list=[]
for i in range(n//2):
    lines_list.append(('.|.'*(j)).center(m,'-'))
    j+=2
for line in lines_list:
    print(line)
print('WELCOME'.center(m,'-'))
for line in reversed(lines_list):
    print(line)
