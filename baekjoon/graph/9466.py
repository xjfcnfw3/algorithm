import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
t = int(input())

def dfs(current):
    global result
    visited[current] = True
    team.append(current)
    next_people = graph[current]

    if visited[next_people]:
        if next_people in team:
            result += len(team[team.index(next_people):])
    else:
        dfs(next_people)

for _ in range(t):
    n = int(input())
    graph = [0] * (n + 1)
    arr = list(map(int, input().split()))
    result = 0
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        graph[i] = arr[i - 1]
    for i in range(1, n + 1):
        if visited[i]:
            continue
        team = []
        dfs(i)
    print(n - result)
