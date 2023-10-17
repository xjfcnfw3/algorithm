def hold(x, y, stone):
    global n
    if stone == 1:
        black.add((x, y))
    else:
        white.add((x, y))
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if stone == 1 and (nx, ny) in white:
                result = False
                cx, cy = nx, ny
                arr = []
                while 0 <= cx < n and 0 <= cy < n:
                    if (cx, cy) in white:
                        arr.append((cx, cy))
                    elif (cx, cy) in black:
                        result = True
                        break
                    else:
                        break
                    cx, cy = cx + dx, cy + dy
                if result:
                    for s in arr:
                        white.remove(s)
                        black.add(s)
            elif stone == 2 and (nx, ny) in black:
                result = False
                cx, cy = nx, ny
                arr = []
                while 0 <= cx < n and 0 <= cy < n:
                    if (cx, cy) in black:
                        arr.append((cx, cy))
                    elif (cx, cy) in white:
                        result = True
                        break
                    else:
                        break
                    cx, cy = cx + dx, cy + dy
                if result:
                    for s in arr:
                        black.remove(s)
                        white.add(s)

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    black = set()
    white = set()
    white.add((n // 2 - 1, n // 2 - 1))
    white.add((n // 2, n // 2))
    black.add((n // 2, n // 2 - 1))
    black.add((n // 2 - 1, n // 2))
    for _ in range(m):
        y, x, stone = map(int, input().split())
        hold(x - 1, y - 1, stone)
    print("#{} {} {}".format(test_case, len(black), len(white)))