n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []


def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    current = 0
    for i in range(start, n):
        if not visited[i] and current != arr[i]:
            visited[i] = True
            temp.append(arr[i])
            current = arr[i]
            dfs(i + 1)
            visited[i] = False
            temp.pop()


dfs(0)
