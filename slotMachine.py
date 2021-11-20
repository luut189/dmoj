quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

count = 0

while quarters > 0:
    quarters-=1
    first+=1
    count+=1
    if first == 35:
        quarters += 30
        first = 0
    if quarters == 0: continue

    quarters-=1
    second+=1
    count+=1
    if second == 100:
        quarters+=60
        second = 0
    if quarters == 0: continue

    quarters-=1
    third+=1
    count+=1
    if third == 10:
        quarters+=9
        third = 0
    if quarters == 0: continue

print("Martha plays",count,"times before going broke.")