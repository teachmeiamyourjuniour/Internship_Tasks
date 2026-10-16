# 12.Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    if len(array)== n:
        n_array=set(array)
        c=(sum(n_array)/len(n_array))
        return c
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
