def dfs(graph, v, visied):
    visied[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visied[i]:
            dfs(graph, i, visied)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9


dfs(graph, 1, visited)