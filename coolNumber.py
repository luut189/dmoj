import math

a = int(input())
b = int(input())

count = 0

for i in range(a, b, 1):
    x = math.ceil(math.sqrt(i))
    y = math.ceil(math.pow(i, 1/3.))

    if math.pow(x, 2) == i and math.pow(y, 3) == i:
        count+=1

print(count)