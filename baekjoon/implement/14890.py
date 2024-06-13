import sys
input = sys.stdin.readline
n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def check_line(line):
    global n, l
    visited = [False] * n

    for i in range(1, n):
        if abs(line[i - 1] - line[i]) > 1:
            return False
        else:
            if (line[i - 1] - line[i]) == 1:
                for j in range(l):
                    if i + j >= n:
                        return False
                    if line[i] != line[i + j]:
                        return False
                    if visited[i + j]:
                        return False
                    else:
                        visited[i + j] = True
            elif (line[i - 1] - line[i]) == -1:
                for j in range(l):
                    if i - 1 - j < 0:
                        return False
                    if line[i - 1] != line[i - 1 - j]:
                        return False
                    if visited[i - 1 - j]:
                        return False
                    else:
                        visited[i - j - 1] = True
    return True
result = 0
for i in range(n):
    if check_line(board[i]):
        result += 1
for j in range(n):
    if check_line([board[i][j] for i in range(n)]):
        result += 1
print(result)
