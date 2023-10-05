def dfs(current, point, index):
    global n, ka, result
    if current > ka:
        return
    result = max(point, result)
    if index < n:
        dfs(current + arr[index][1], point + arr[index][0], index + 1)
        dfs(current, point, index + 1)
T = int(input())

for test_case in range(1, T + 1):
    n, ka = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    dfs(0, 0, 0)
    print("#" + str(test_case) + " " + str(result))