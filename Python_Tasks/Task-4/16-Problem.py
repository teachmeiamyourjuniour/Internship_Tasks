# 16.Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n=int(input())
    if 2<=n<=5:
        j=[]
        b=88
        g=[]
        f=[]
        for _ in range(n):
            name = input()
            score = float(input())
            j.append([name,score])
            g.append(score)
        for x in j:
            if x[1]<b:
                if x[1]>min(g):
                    b=x[1]
        for x in j:
            if x[1]==b:
                f.append(x[0])
        for x in sorted(f):
            print(x)
