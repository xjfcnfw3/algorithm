def solution(commands):
    answer = []
    arr = []
    meta = []
    for i in range(50):
        row = []
        row_m = []
        for j in range(50):
            row.append([i, j])
            row_m.append(["EMPTY", [[i, j]]])
        arr.append(row)
        meta.append(row_m)

    def merge(command):
        r1, c1, r2, c2 = map(int, command)
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        x1, y1 = arr[r1][c1]
        x2, y2 = arr[r2][c2]
        v1 = meta[x1][y1][0]
        v2 = meta[x2][y2][0]
        if r1 < r2 or (r1 == r2 and c1 < c2):
            x1, y1 = arr[r1][c1]
            x2, y2 = arr[r2][c2]
            if x1 == x2 and y1 == y2:
                return
            arr[r2][c2] = [x1, y1]
            for a, b in meta[x2][y2][1]:
                meta[x1][y1][1].append([a, b])
                arr[a][b] = [x1, y1]
        else:
            x1, y1 = arr[r1][c1]
            x2, y2 = arr[r2][c2]
            if x1 == x2 and y1 == y2:
                return
            arr[r1][c1] = [x1, y1]
            for a, b in meta[x2][y2][1]:
                meta[x1][y1][1].append([a, b])
                arr[a][b] = [x1, y1]
        if v1 != "EMPTY" and v2 != "EMPTY":
            x, y = arr[r1][c1]
            meta[x][y][0] = v1
        elif v1 != "EMPTY":
            x, y = arr[r1][c1]
            meta[x][y][0] = v1
        elif v2 != "EMPTY":
            x, y = arr[r1][c1]
            meta[x][y][0] = v2

    def update(command):
        if len(command) == 3:
            x, y, v = command
            x, y = arr[int(x) - 1][int(y) - 1]
            meta[x][y][0] = v
        else:
            v1, v2 = command
            for i in range(50):
                for j in range(50):
                    if meta[i][j][0] == v1:
                        meta[i][j][0] = v2

    def print_value(command):
        x, y = map(int, command)
        x, y = x - 1, y - 1
        x, y = arr[x][y]
        value = meta[x][y][0]
        answer.append(value)

    def unmerge(command):
        x, y = map(int, command)
        x, y = x - 1, y - 1
        cx, cy = arr[x][y]
        value, cells = meta[cx][cy]
        for a, b in cells:
            arr[a][b] = [a, b]
            meta[a][b] = ["EMPTY", [[a, b]]]
            if a == x and b == y:
                meta[x][y][0] = value

    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            update(command[1:])
        elif command[0] == "MERGE":
            merge(command[1:])
        elif command[0] == "PRINT":
            print_value(command[1:])
        else:
            unmerge(command[1:])
    return answer