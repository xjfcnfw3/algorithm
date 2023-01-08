n = int(input())
board = [0] * n
result = 0


def check(num):
    for i in range(num):
        if (board[num] == board[i]) or (num - i == abs(board[num] - board[i])):
            return False
    return True


def n_queen(depth):
    global result

    if depth == n:
        result += 1
        return

    for i in range(n):
        board[depth] = i
        if check(depth):
            n_queen(depth + 1)


n_queen(0)
print(result)
