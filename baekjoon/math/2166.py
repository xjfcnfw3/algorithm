import sys
input = sys.stdin.readline
x, y = [], []
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

rx, ry = 0, 0
for i in range(n):
    rx += x[i] * y[i + 1]
    ry += y[i] * x[i + 1]

print(round(abs((rx-ry)/2), 1))