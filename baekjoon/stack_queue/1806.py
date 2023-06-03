from collections import deque
import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

if sum(arr) < s:
    print(0)
    exit()
elif max(arr) >= s:
    print(1)
    exit()

q = deque()
result = sys.maxsize
current = 0
for i in range(n):
    q.append(arr[i])
    current += arr[i]
    if current >= s:
        while current >= s:
            result = min(len(q), result)
            current -= q[0]
            q.popleft()
print(result)