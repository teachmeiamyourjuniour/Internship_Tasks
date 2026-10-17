# 20.Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

T = int(input())
for i in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    stackable = True
    j, k = 0, n-1
    top = max(blocks[j], blocks[k])+1
    while stackable and j - k <= 0:
        if blocks[j] > blocks[k] and blocks[j] <= top:
            top = blocks[j]
            j += 1
        elif blocks[k] > blocks[j] and blocks[k] <= top:
            top = blocks[k]
            k -= 1
        elif blocks[j] == blocks[k] and blocks[j] <= top:
            top = blocks[j]
            j += 1
        else:
            stackable = False
        
    if stackable:
        print('Yes')
    else:
        print('No')
