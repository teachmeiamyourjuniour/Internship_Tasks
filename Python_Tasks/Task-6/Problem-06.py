# 6.Print Function
# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    if n>0 and n<151:
        for i in range(1,n+1):
            print(i,end='')
