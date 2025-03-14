import math


def solution(r1, r2):
    answer = 0

    for i in range(1, r2 + 1):
        s = 0
        if i < r1:
            s = math.ceil((r1 ** 2 - i ** 2) ** (1 / 2))
        e = int((r2 ** 2 - i ** 2) ** (1 / 2))
        answer += e - s + 1
    return answer * 4