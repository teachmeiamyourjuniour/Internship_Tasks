# 12.Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
for _ in range(0, int(input())):
    command = input().split()
    match command[0]:
        case 'remove':
            s.remove(int(command[1]))
        case 'discard':
            s.discard(int(command[1]))
        case 'pop':
            s.pop()
print(sum(s))
