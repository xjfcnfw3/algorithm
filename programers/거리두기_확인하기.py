def solution(places):
    answer = []
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(x, y, depth, place):
        visited[x][y] = True
        if depth == 2:
            if place[x][y] == "P":
                return False
            else:
                return True

        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny] and place[nx][ny] != "X":
                    if place[nx][ny] == "P":
                        return False
                    if not dfs(nx, ny, depth + 1, place):
                        return False
        return True

    for place in places:
        result = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    visited = [[False] * 5 for _ in range(5)]
                    if not dfs(i, j, 0, place):
                        result = False
                        break
        if result:
            answer.append(1)
        else:
            answer.append(0)
    return answer