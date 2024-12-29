import sys

input = sys.stdin.readline
stk = []
n = int(input())
result = 0

for i in range(n):
    a, b = map(int, input().split())
    while stk and stk[-1] > b:
        stk.pop()
    if stk and stk[-1] == b:
        continue
    if b > 0:
        stk.append(b)
        result += 1
print(result)
