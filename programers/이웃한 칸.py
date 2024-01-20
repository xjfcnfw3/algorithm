def solution(board, h, w):
    answer = 0
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = h + dx, w + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            if board[nx][ny] == board[h][w]:
                answer += 1
    return answer