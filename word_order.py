from collections import OrderedDict
d = OrderedDict()
n = int(input())

for i in range(n):
    word = input()
    d[word] = d.get(word,0) + 1
print(len(d.keys()))
for j,k in d.items(): 
    print(k,end= " ")
