import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

dic = {}
result = 0

for a in A:
    for b in B:
        ab = a + b
        if ab in dic:
            dic[ab] += 1
        else:
            dic[ab] = 1
for c in C:
    for d in D:
        cd = (c + d) * -1
        if cd in dic:
            result += dic[cd]
print(result)
