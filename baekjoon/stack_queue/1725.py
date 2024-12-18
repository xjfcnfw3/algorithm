import sys

input = sys.stdin.readline
n = int(input())
stk = []
result = 0
for i in range(n):
    num = int(input())
    start = i
    while stk and stk[-1][0] > num:
        height, start = stk.pop()
        if (i - start) * height > result:
            result = (i - start) * height
    if not stk or stk[-1][0] != num:
        stk.append((num, start))
while stk:
    height, start = stk.pop()
    if (n - start) * height > result:
        result = (n - start) * height
print(result)