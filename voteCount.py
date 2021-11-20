vote = int(input())
type = input()

countA = 0
countB = 0
for i in range(0, vote, 1):
    if type[i] == 'A':
        countA +=1
    elif type[i] == 'B':
        countB+=1

if countA > countB:
    print("A")
elif countB > countA:
    print("B")
else:
    print("Tie")