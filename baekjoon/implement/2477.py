n = int(input())

x = 0
y = 0
max_row = 0
max_col = 0
arr = [[0, 0]]

for i in range(6):
    direction, dist = map(int, input().split())

    if direction == 1:
        x += dist
        max_row = max(max_row, dist)
    elif direction == 2:
        x -= dist
        max_row = max(max_row, dist)
    elif direction == 3:
        y -= dist
        max_col = max(max_col, dist)
    elif direction == 4:
        y += dist
        max_col = max(max_col, dist)
    arr.append([x, y])

arr.pop()

hall_row = 0
hall_col = 0

sorted_x = sorted(arr, key=lambda x : x[0])
sorted_y = sorted(arr, key=lambda x : x[1])

start_x = sorted_x[0][0]
start_y = sorted_y[0][1]

for i in range(len(sorted_x)):
    if sorted_x[i][0] != start_x:
        hall_col = abs(sorted_x[i][1] - sorted_x[i + 1][1])
        break
for i in range(len(sorted_y)):
    if sorted_y[i][1] != start_y:
        hall_row = abs(sorted_y[i][0] - sorted_y[i + 1][0])
        break
print(n * (max_row * max_col - hall_row * hall_col))