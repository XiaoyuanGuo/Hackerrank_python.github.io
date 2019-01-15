
import re

pattern = r"[789]\d{9}$"

n = int(input())
for _ in range(n):
    if bool(re.match(pattern, input())):
        print("YES")
    else:
        print("NO")
