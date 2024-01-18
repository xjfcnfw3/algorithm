from collections import deque
def bfs(x, y, visited, land, answer):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    ground = [y]
    result = 0
    while q:
        cx, cy = q.popleft()
        result += 1
        if cy not in ground:
            ground.append(cy)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and not visited[nx][ny] and land[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
    for num in ground:
        answer[num] += result
def solution(land):
    answer = [0] * len(land[0])
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j]:
                bfs(i, j, visited, land, answer)
    return max(answer)