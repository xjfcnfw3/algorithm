import sys

sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * a
li = []

arr.sort()

def dfs(depth):
    if depth == b:
        print(*li)
        return
    temp = 0
    for i in range(a):
        if not visited[i] and temp != arr[i]:
            visited[i] = True
            li.append(arr[i])
            temp = arr[i]
            dfs(depth + 1)
            visited[i] = False
            li.pop()

dfs(0)

