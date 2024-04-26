# 움직이는 좌표 저장 -> 최대 x, 최대 y, 최소 x, 최소 y를 직접 구한다.

n = int(input())
x, y = 0, 0

d = {
    0 : (-1, 0),
    1 : (0, 1),
    2 : (1, 0),
    3 : (0, -1)
}

direction = 2
road = set()
road.add((0, 0))
x1, y1, x2, y2 = 0, 0, 0, 0

for c in input().rstrip():
    if c == "R":
        direction = (direction + 1) % 4
    elif c == "L":
        direction = (direction - 1) % 4
    else:
        x, y = x + d[direction][0], y + d[direction][1]
        road.add((x, y))
        x1, y1, x2, y2 = min(x1, x), min(y1, y), max(x2, x), max(y2, y)

row, col = x2 - x1 + 1, y2 - y1 + 1
move_x, move_y = 0 if x1 >= 0 else -x1, 0 if y1 >= 0 else -y1

result = [['#'] * col for _ in range(row)]

for x, y in road:
    result[x + move_x][y + move_y] = "."

for i in range(row):
    for j in range(col):
        print(result[i][j], end ="")
    print()