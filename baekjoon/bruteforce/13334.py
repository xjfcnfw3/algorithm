import sys, heapq

input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(int(input()))]
roads = []
d = int(input())
for i in range(len(arr)):
    x, y = arr[i]
    if abs(x - y) > d:
        continue
    if x < y:
        roads.append([x, y])
    else:
        roads.append([y, x])
roads.sort(key=lambda x: x[1])
result = 0
q = []
for road in roads:
    if not q:
        heapq.heappush(q, road)
    else:
        while q[0][0] < road[1] - d:
            heapq.heappop(q)
            if not q:
                break
        heapq.heappush(q, road)
    result = max(result, len(q))
print(result)
