# 20.Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
regex_pattern = r"^[789]\d{9}$"

for _ in range(int(input())):
        print("YES" if (re.match(regex_pattern, input())) else "NO")
