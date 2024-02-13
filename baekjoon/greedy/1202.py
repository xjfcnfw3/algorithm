import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jews = []
bags = []
for _ in range(n):
    heapq.heappush(jews, list(map(int, input().split())))
bags = [int(input()) for _ in range(k)]

bags.sort()
result = 0
tmp_jew = []
for bag in bags:
    while jews and jews[0][0] <= bag:
        heapq.heappush(tmp_jew, -heapq.heappop(jews)[1])
    if tmp_jew:
        result -= heapq.heappop(tmp_jew)
    elif not jews:
        break
print(result)