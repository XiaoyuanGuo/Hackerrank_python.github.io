# Enter your code here. Read input from STDIN. Print output to STDOUT

m , n = map(int, input().split(" "))
t = []
for _ in range(n):
    t.append([float(x) for x in input().split(" ")])
st = zip(*t)
for i in st:
    print(sum(i)/n)
   
