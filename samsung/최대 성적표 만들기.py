import heapq
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    q = []
    for i in range(n):
        heapq.heappush(q, -arr[i])
    result = 0
    for _ in range(k):
        result -= heapq.heappop(q)
    print("#{} {}".format(test_case, result))