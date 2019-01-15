import numpy

n,m,p = map(int, input().split(" "))
A = []
B = []
for _ in range(n):
    A.append([int(x) for x in input().split(" ")])
A = numpy.array(A)

for _ in range(m):
    B.append([int(x) for x in input().split(" ")])
B = numpy.array(B)

C = numpy.concatenate((A, B), axis = 0)

print(C)

