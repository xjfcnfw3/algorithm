import heapq
def solution(n, k, enemy):
    q = []
    answer = 0
    for i in enemy:
        if len(q) >= k and n < min(i, q[0]):
            break
        heapq.heappush(q, i)
        answer += 1
        if len(q) > k:
            n -= heapq.heappop(q)
            if n <= 0:
                break
    return answer