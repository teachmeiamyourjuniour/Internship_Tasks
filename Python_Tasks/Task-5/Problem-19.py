# 19.Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    j = 0
    while j < len(string):
        substring = ""
        for char in string[j : j+k]:
            if char not in substring:
                substring += char
        print(substring)
        j += k    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
