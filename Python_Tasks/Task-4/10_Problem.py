# 10.Find a String
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    if 1<=len(string)<=200:
        
        count = 0
        start = 0
        while True:
            start = string.find(sub_string, start)
            if start == -1:  # No more matches found
                break
            count += 1
            start += 1  # Move forward by 1 to catch overlaps

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
