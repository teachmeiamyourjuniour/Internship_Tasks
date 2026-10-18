# 9.What's Your Name?
# https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    # Write your code here
    if (len(first) and len(last)) <= 10:
        c=f"Hello {first} {last}! You just delved into python."
        print(c)
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
