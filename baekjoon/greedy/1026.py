import heapq
n = int(input())

a = list(map(int, input().split()))
q = []
for num in a:
    heapq.heappush(q, num)
b = list(map(int, input().split()))
b.sort(reverse=True)
result = 0
for num in b:
    result += num * heapq.heappop(q)

print(result)