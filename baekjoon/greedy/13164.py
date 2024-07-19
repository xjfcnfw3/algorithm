import heapq
n, k = map(int, input().split())
arr = list(map(int, input().split()))

q = []

for i in range(n - 1):
    heapq.heappush(q, -1 * (arr[i + 1] - arr[i]))

for _ in range(k - 1):
    heapq.heappop(q)

print(-1 * sum(q))