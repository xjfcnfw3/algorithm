from collections import deque


def solution(n, k):
    q = deque()

    def check(num):
        if num == 1:
            return 0
        for i in range(2, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                return 0
        return 1

    while n >= 1:
        a = n % k
        q.appendleft(str(a))
        n = n // k
    answer = 0
    result = "".join(q)
    result = result.split("0")

    for i in result:
        if i:
            answer += check(int(i))
    return answer