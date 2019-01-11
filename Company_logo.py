import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict


if __name__ == '__main__':
    s = input()
    tmp = [s[i] for i in range(len(s))]
    res = Counter(tmp)
    t = OrderedDict(res.most_common())
    k = 0
    for i,j in t.items():
        if k < 3:
            print(i,j)
        k += 1
