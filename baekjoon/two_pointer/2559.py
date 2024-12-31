import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, k - 1
answer = sum(arr[:k])
temp = answer
while end < n - 1:
    temp -= arr[start]
    end += 1
    start += 1
    temp += arr[end]
    answer = max(answer, temp)
print(answer)