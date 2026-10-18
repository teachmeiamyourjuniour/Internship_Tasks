# 1.Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem



if __name__ == '__main__':
    n = int(input())
    if 1<=n and n<=100:
        if n%2==0:
            if n>20:
                v='Not Weird'
            elif 2<=n and n<=5:
                v='Not Weird'
            elif 6<=n and n<=20:
                v='Weird'
        else:
            v='Weird'
        print(v)
