from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
foods = [list(map(int, input().split())) for _ in range(n)]
board = [[5] * n for _ in range(n)]

tree = [[deque() for _ in range(n)] for _ in range(n)]
death_tree = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    tree[x][y].append(z)


def spring_and_summer():
    global n
    for x in range(n):
        for y in range(n):
            if not tree[x][y]:
                continue
            trees_len = len(tree[x][y])
            for i in range(trees_len):
                if board[x][y] < tree[x][y][i]:
                    for _ in range(i, trees_len):
                        death_tree[x][y].append(tree[x][y].pop())
                    break
                else:
                    board[x][y] -= tree[x][y][i]
                    tree[x][y][i] += 1
            while death_tree[x][y]:
                board[x][y] += death_tree[x][y].pop() // 2

def fall_and_winter():
    global n
    for x in range(n):
        for y in range(n):
            board[x][y] += foods[x][y]
            for age in tree[x][y]:
                if age % 5 == 0:
                    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)


def print_result():
    global n
    result = 0
    for x in range(n):
        for y in range(n):
            result += len(tree[x][y])
    print(result)


for _ in range(k):
    spring_and_summer()
    fall_and_winter()
print_result()
