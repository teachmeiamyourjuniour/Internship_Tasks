# 18.Lists
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    h=[]
    while(N!=0):
        f=list(input().split())
        if f[0]=='print':
            print(h)
        elif f[0]=='insert':
            h.insert(int(f[1]),int(f[2]))
        elif f[0]=='sort':
            h.sort()
        elif f[0]=='append':
            h.append(int(f[1]))
        elif f[0]=='pop':
            h.pop()
        elif f[0]=='reverse':
            h.reverse()
        elif f[0]=='remove':
            h.remove(int(f[1]))
        N-=1

