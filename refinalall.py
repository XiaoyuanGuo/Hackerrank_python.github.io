# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

vowels = "AEIOUaeiou"
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
substrings = re.findall(r'(?<=[' + consonants + '])[' + vowels + ']{2,}(?=[' + consonants + '])', input())
if substrings is not None:
    if len(substrings) > 0:
        for s in substrings:
            print(s)
    else:
        print(-1)
else:
    print(-1)


