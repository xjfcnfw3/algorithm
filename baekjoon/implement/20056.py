import sys
from collections import defaultdict
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())

fire_ball = defaultdict(list)

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fire_ball[(r - 1, c - 1)].append((m, s, d))
def move():
    global n
    new_fire_ball = defaultdict(list)
    for r, c in fire_ball.keys():
        for i in range(len(fire_ball[(r, c)])):
            m, s, d = fire_ball[(r, c)][i]
            nr, nc = (r + dx[d] * s) % n, (c + dy[d] * s) % n
            new_fire_ball[(nr, nc)].append((m, s, d))
    return new_fire_ball

def new_fire():
    new_fire_ball = defaultdict(list)
    for r, c in fire_ball.keys():
        if len(fire_ball[(r, c)]) == 1:
            new_fire_ball[(r, c)].append(fire_ball[(r, c)][0])
            continue
        weight, speed, odd, even= 0, 0, 0, 0
        size = len(fire_ball[(r, c)])
        for i in range(size):
            m, s, d = fire_ball[(r, c)][i]
            weight += m
            speed += s
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd == size or even == size:
            nd = [0, 2, 4, 6]
        else:
            nd = [1, 3, 5, 7]
        if weight // 5:
            for d in nd:
                new_fire_ball[(r, c)].append((weight // 5, speed // size, d))
    return new_fire_ball

def check_weight():
    result = 0
    for r, c in fire_ball.keys():
        for i in range(len(fire_ball[(r, c)])):
            result += fire_ball[(r, c)][i][0]
    return result

for _ in range(k):
    fire_ball = move()
    fire_ball = new_fire()
print(check_weight())