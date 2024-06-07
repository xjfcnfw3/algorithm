import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def two_pooling(x1, y1, x2, y2):
    temp = [board[x1][y1], board[x1][y2], board[x2][y1], board[x2][y2]]
    temp.sort()
    return temp[-2]


def pooling():
    result = []
    for i in range(0, len(board), 2):
        row = []
        for j in range(0, len(board), 2):
            row.append(two_pooling(i, j, i + 1, j + 1))
        result.append(row)
    return result


while len(board) != 1:
    board = pooling()
print(board[0][0])
