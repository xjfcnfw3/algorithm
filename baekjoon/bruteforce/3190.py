from collections import deque
n = int(input())
apples = set()
for _ in range(int(input())):
    a_x, a_y = map(int, input().split())
    apples.add((a_x - 1, a_y - 1))
direction = 1
# 0 북, 1 동, 2 남, 3 서
x, y = 0, 0
snake = deque()
snake.append((x, y))
result = 0
complete = False

def move_snake(x, y):
    if (x, y) in apples:
        apples.remove((x, y))
        snake.append((x, y))
    else:
        snake.popleft()
        snake.append((x, y))

def move(t):
    global direction, x, y, n, result, complete

    for i in range(t):
        result += 1
        if direction == 0:
            x -= 1
            if x < 0:
                complete = True
                return
            elif (x, y) in snake:
                complete = True
                return
            move_snake(x, y)
        elif direction == 1:
            y += 1
            if y >= n:
                complete = True
                return
            elif (x, y) in snake:
                complete = True
                return
            move_snake(x, y)
        elif direction == 2:
            x += 1
            if x >= n:
                complete = True
                return
            elif (x, y) in snake:
                complete = True
                return
            move_snake(x, y)
        else:
            y -= 1
            if y < 0:
                complete = True
                return
            elif (x, y) in snake:
                complete = True
                return
            move_snake(x, y)

for _ in range(int(input())):
    t, next_direction = input().split()
    t = int(t) - result
    move(t)
    if next_direction == "D":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    if complete:
        break
if not complete:
    move(n)
print(result)
