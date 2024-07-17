import heapq, sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
q = []

for p, d in arr:
    heapq.heappush(q, p)
    if len(q) > d:
        heapq.heappop(q)
print(sum(q))