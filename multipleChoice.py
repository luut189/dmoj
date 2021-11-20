qNum = int(input())

quest = [None] * qNum
ans = [None] * qNum

for i in range(0, qNum, 1):
    quest[i] = input()

for i in range(0, qNum, 1):
    ans[i] = input()

count = 0

for i in range(0, qNum, 1):
    if quest[i] == ans[i]:
        count+=1

print(count)
