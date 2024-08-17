import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    arr = [list(map(int, input().split())) for _ in range(m)]
    result = 0
    arr.sort(key=lambda x:(x[1], x[0]))
    for a, b in arr:
        for i in range(a, b + 1):
            if not visited[i]:
                visited[i] = True
                result += 1
                break
    print(result)