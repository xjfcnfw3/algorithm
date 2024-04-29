# 빈 방을 생성 (배열 형식으로)
# heapq연산으로 플레이어 이름 순으로 정렬
# 레벨을 기준으로 +-10인지 체크
# 맞으면 해당 방, 틀리면 다른 방

p, m = map(int, input().split())

started = []
rooms = []


def print_room(i):
    if started[i]:
        print("Started!")
    else:
        print("Waiting!")
    rooms[i].sort(key=lambda x: x[1])
    for j in range(len(rooms[i])):
        print(*rooms[i][j])


def check_start(i):
    global m
    if len(rooms[i]) == m:
        started[i] = True


def check_room(i, level):
    global m
    if started[i]:
        return False
    if len(rooms[i]) >= m:
        return False
    if int(rooms[i][0][0]) + 10 < level or int(rooms[i][0][0]) - 10 > level:
        return False
    return True


for level, nickname in [input().split() for _ in range(p)]:
    if not started:
        started.append(False)
        rooms.append([[level, nickname]])
        check_start(0)
        continue
    offset = False

    for i in range(len(rooms)):
        if check_room(i, int(level)):
            rooms[i].append([level, nickname])
            check_start(i)
            offset = True
            break
    if not offset:
        started.append(False)
        rooms.append([[level, nickname]])
        check_start(len(rooms) - 1)

for i in range(len(rooms)):
    print_room(i)
