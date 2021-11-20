a = input()
count = 0

for i in range(len(a)):
    if a[i] == 'I' or a[i] == 'O' or a[i] == 'S' or a[i] == 'H' or a[i] == 'Z' or a[i] == 'X' or a[i] == 'N':
        count+=1

if count == len(a):
    print("YES")
else:
    print("NO")