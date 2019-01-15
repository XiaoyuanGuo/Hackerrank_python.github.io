import numpy

myinput = [float(x) for x in input().split(" ")]
x = float(input())
#The polyval tool evaluates the polynomial at specific value.
print(numpy.polyval(myinput,x))

