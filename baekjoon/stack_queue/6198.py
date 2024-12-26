n = int(input())
stk = []
result = 0
for _ in range(n):
    num = int(input())

    while stk and stk[-1][0] <= num:
        number, count = stk.pop()
        if stk:
            stk[-1][1] += count
        result += count

    if not stk:
        stk.append([num, 0])
    else:
        stk[-1][1] += 1
        stk.append([num, 0])

while stk:
    number, count = stk.pop()
    if stk:
        stk[-1][1] += count
    result += count

print(result)