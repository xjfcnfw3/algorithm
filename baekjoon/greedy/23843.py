import heapq
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
q = []

for i in reversed(range(len(arr))):
    if len(q) < m:
        heapq.heappush(q, arr[i])
    else:
        end = heapq.heappop(q)
        heapq.heappush(q, end + arr[i])
print(max(q))