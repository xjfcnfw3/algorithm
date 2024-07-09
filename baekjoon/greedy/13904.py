import heapq, sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()
q = []
for day, val in arr:
    heapq.heappush(q, val)
    if day < len(q):
        heapq.heappop(q)
print(sum(q))