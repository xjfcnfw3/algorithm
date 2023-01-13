from bisect import bisect_left

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
s = [-1000000001]
max_len = 0

for i in range(1, n + 1):
    if arr[i] > s[-1]:
        s.append(arr[i])
        max_len = len(s) - 1
        dp[i] = max_len
    else:
        dp[i] = bisect_left(s, arr[i])
        s[dp[i]] = arr[i]
    print(*s)

print(max_len)
result = []
for i in range(n, 0, -1):
    if dp[i] == max_len:
        result.append(arr[i])
        max_len -= 1
result.reverse()
print(*result)
