import heapq

T = 10

for test_case in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    max_q = []
    min_q = []
    for n in arr:
        heapq.heappush(max_q, -n)
        heapq.heappush(min_q, n)
    for _ in range(num):
        a = - heapq.heappop(max_q)
        b = heapq.heappop(min_q)
        heapq.heappush(max_q, -(a - 1))
        heapq.heappush(min_q, (b + 1))

    result = - heapq.heappop(max_q) - heapq.heappop(min_q)
    print("#" + str(test_case) + " " + str(result))

T = 10

for test_case in range(1, T + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    max_q = []
    min_q = []
    for n in arr:
        heapq.heappush(max_q, -n)
        heapq.heappush(min_q, n)
    for _ in range(num):
        a = - heapq.heappop(max_q)
        b = heapq.heappop(min_q)
        heapq.heappush(max_q, -(a - 1))
        heapq.heappush(min_q, (b + 1))

    result = - heapq.heappop(max_q) - heapq.heappop(min_q)
    print("#" + str(test_case) + " " + str(result))