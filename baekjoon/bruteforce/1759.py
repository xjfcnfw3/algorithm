from itertools import combinations
l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
result = list(combinations(arr, l))

m = {'a', 'e', 'i', 'o', 'u'}
n = set()
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in m:
        n.add(chr(i))

for i in result:
    a = False
    b = False
    t = 0
    for j in i:
        if j in m:
            a = True
        elif j in n:
            t += 1
        if t == 2:
            b = True
    if a and b:
        print(''.join(i))