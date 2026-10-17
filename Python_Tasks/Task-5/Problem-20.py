# 20.Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque
def possible_to_make_pillar(blocks):
    while blocks:
        if blocks[-1] >= blocks[0]:
            lastcube = blocks[-1]
            blocks.pop()
        elif blocks[0] > blocks[-1]:
            lastcube = blocks[0]
            blocks.popleft()
        if blocks and (blocks[0]> lastcube or blocks[-1] > lastcube):
            return "No"
    return "Yes"
            

T = int(input())
for _ in range(T):
    _ = input()
    blocks = deque(map(int,input().split()))
    print(possible_to_make_pillar(blocks))
        
    if stackable:
        print('Yes')
    else:
        print('No')
