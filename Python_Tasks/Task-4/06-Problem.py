# 6.Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    c=-300
    for x in arr:
        if x>c :
            if x<max(arr):
                c=x
    print(c)
