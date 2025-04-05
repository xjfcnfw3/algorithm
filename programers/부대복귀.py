from collections import deque, defaultdict


def solution(n, roads, sources, destination):
    visit = [-1] * (n + 1)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([destination])
    visit[destination] = 0
    while q:
        now = q.popleft()

        for node in graph[now]:
            if visit[node] == -1:
                visit[node] = visit[now] + 1
                q.append(node)

    return [visit[i] for i in sources]