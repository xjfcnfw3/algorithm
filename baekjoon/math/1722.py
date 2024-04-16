import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
factorial = [1] * 21

for i in range(1, n + 1):
    factorial[i] = factorial[i - 1] * i
if arr[0] == 1:
    k = arr[1]
    result = []
    visited = [False] * (n + 1)
    for i in range(n, 0, -1):
        num = 1
        while num <= n and visited[num]:
            num += 1
        while k > factorial[i - 1]:
            k -= factorial[i - 1]
            num += 1
            while visited[num]:
                num += 1
        visited[num] = True
        result.append(num)
    print(*result)
else:
    visited = [False] * (n + 1)
    li = arr[1:]
    result = 1
    for i in range(n):
        num = 1
        while visited[num]:
            num += 1
        while num != li[i]:
            result += factorial[n - i - 1]
            num += 1
            while visited[num]:
                num += 1
        visited[num] = True
    print(result)