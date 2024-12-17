import sys

input = sys.stdin.readline
n = int(input())
stk = []
result = 0
for _ in range(n):
    num = int(input())

    while stk and stk[-1][0] < num:
        result += stk.pop()[1]
    if not stk:
        stk.append((num, 1))
        continue
    if stk[-1][0] == num:
        cnt = stk.pop()[1]
        result += cnt
        if stk:
            result += 1
        stk.append((num, cnt + 1))
    else:
        stk.append((num, 1))
        result += 1
print(result)