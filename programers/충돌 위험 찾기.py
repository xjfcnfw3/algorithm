def solution(points, routes):
    answer = set()
    point_dict = {}
    arr = [[[] for _ in range(101)] for _ in range(101)]
    for i in range(len(points)):
        point_dict[i + 1] = points[i]
    for route in routes:
        x, y = point_dict[route[0]]
        time = 0
        if time in arr[x][y]:
            if (x, y, time) not in answer:
                answer.add((x, y, time))
        else:
            arr[x][y].append(time)

        for i in range(len(route)):
            next_x, next_y = point_dict[route[i]]
            move_x, move_y = next_x - x, next_y - y
            dx, dy = 0, 0
            if move_x != 0:
                dx = move_x // abs(move_x)
            if move_y != 0:
                dy = move_y // abs(move_y)

            for _ in range(abs(move_x)):
                x += dx
                time += 1
                if time in arr[x][y]:
                    if (x, y, time) not in answer:
                        answer.add((x, y, time))
                else:
                    arr[x][y].append(time)
            for _ in range(abs(move_y)):
                y += dy
                time += 1
                if time in arr[x][y]:
                    if (x, y, time) not in answer:
                        answer.add((x, y, time))
                else:
                    arr[x][y].append(time)
    return len(answer)