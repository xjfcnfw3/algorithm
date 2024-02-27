from collections import deque


def solution(n, computers):
    visited = [False for _ in range(len(computers))]

    def bfs(start):
        q = deque([start])
        while q:
            node = q.popleft()
            visited[node] = True

            for i in range(len(computers)):
                if computers[node][i] == 1 and not visited[i]:
                    q.append(i)

    answer = 0
    for i in range(len(computers)):
        if not visited[i]:
            answer += 1
            bfs(i)
    return answer