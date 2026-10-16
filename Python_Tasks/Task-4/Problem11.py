# 11.String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isdigit = False 
    islower = False 
    isupper = False 

    for char in s :
        if char.isalnum():
            isalnum = True 
        if char.isalpha():
            isalpha = True 
        if char.isdigit():
            isdigit = True 
        if char.islower():
            islower = True 
        if char.isupper():
            isupper = True 
    print (isalnum)
    print (isalpha)
    print (isdigit)
    print (islower)
    print (isupper)
