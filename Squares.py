import math

square = int(input())
x = int(math.sqrt(square))
y = int(math.floor(x))

if x * x == square:
    print("The largest square has side length {}.".format(x))
else:
    print("The largest square has side length {}.".format(y))