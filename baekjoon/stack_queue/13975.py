import heapq, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)
    result = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a + b
        heapq.heappush(q, a + b)
    print(result)
