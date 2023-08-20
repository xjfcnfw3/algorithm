import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

if len(q) == 1:
    print(0)
else:
    result = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a + b
        heapq.heappush(q, a + b)

    print(result)