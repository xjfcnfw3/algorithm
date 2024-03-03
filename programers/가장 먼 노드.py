from collections import defaultdict, deque
def bfs(n, graph):
    global max_depth, answer
    visited = [False] * (n + 1)
    visited[1] = True
    q = deque()
    q.append((1, 0))
    while q:
        num, depth = q.popleft()
        if depth > max_depth:
            max_depth = depth
            answer = 1
        elif depth == max_depth:
            answer += 1
        for i in graph[num]:
            if not visited[i]:
                visited[i] = True
                q.append((i, depth + 1))
def solution(n, edge):
    global max_depth, answer
    max_depth = 0
    answer = 0
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    bfs(n, graph)
    return answer