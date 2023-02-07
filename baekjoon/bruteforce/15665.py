n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []


def dfs():
    if len(temp) == m:
        print(*temp)
        return
    current = 0
    for i in range(n):
        if current != arr[i]:
            temp.append(arr[i])
            current = arr[i]
            dfs()
            temp.pop()


dfs()
