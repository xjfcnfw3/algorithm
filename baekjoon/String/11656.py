c = input()
arr = []
for i in range(len(c)):
    arr.append(c[i:])
arr.sort()
for i in arr:
    print(i)