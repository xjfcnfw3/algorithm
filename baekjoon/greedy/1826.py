import heapq, sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
l, p = map(int, input().split())
result = 0
q = []
for a, b in arr:
    if p < a:
        while q and p < a:
            p -= heapq.heappop(q)
            result += 1
        if p < a:
            print(-1)
            exit(0)
    heapq.heappush(q, -b)
while q and p < l:
    p -= heapq.heappop(q)
    result += 1
if p < l:
    print(-1)
else:
    print(result)