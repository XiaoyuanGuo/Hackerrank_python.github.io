
import re

n = int(input())
for i in range(n):
    try:
        print(bool(re.compile(input())))
    except:
        print('False')
