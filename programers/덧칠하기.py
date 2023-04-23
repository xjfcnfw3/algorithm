from collections import deque

def solution(n, m, section):
    answer = 0

    q = deque(section)

    while q:
        start = q.popleft()

        while q and start + m > q[0]:
            q.popleft()
        answer += 1

    return answer