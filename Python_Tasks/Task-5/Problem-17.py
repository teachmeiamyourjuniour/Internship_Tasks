# 17.No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
array_len, set_len  = list(map(int, input().split()))
array = input().split()
set_a = set(input().split())
set_b = set(input().split())
score = 0

for i in array:
    if i in set_a:
        score += 1
    elif i in set_b:
        score -= 1

print(score)
