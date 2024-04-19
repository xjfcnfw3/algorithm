from collections import deque

TOP = 0
LEFT = 6
RIGHT = 2

arr = [deque() for _ in range(4)]

for i in range(4):
    row = list(map(int, list(input())))
    for r in row:
        arr[i].append(r)

t = int(input())


def spin(a, b):
    if b == 1:
        num = arr[a - 1].pop()
        arr[a - 1].appendleft(num)
    else:
        num = arr[a - 1].popleft()
        arr[a - 1].append(num)


def check():
    result = 0
    if arr[0][0] == 1:
        result += 1
    if arr[1][0] == 1:
        result += 2
    if arr[2][0] == 1:
        result += 4
    if arr[3][0] == 1:
        result += 8
    return result


result = 0
for _ in range(t):
    a, b = map(int, input().split())
    moves = [[a, b]]
    for i in range(a + 1, 5):
        if arr[i - 2][RIGHT] != arr[i - 1][LEFT]:
            if (i - a) % 2 == 0:
                moves.append([i, b])
            else:
                moves.append([i, -b])
        else:
            break
    for i in reversed(range(1, a)):
        if arr[i - 1][RIGHT] != arr[i][LEFT]:
            if (a - i) % 2 == 0:
                moves.append([i, b])
            else:
                moves.append([i, -b])
        else:
            break
    for a, b in moves:
        spin(a, b)
result = check()
print(result)
