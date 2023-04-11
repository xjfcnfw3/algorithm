def solution(n, s):
    result = [s // n for _ in range(n)]
    if 0 in result:
        return [-1]
    index = n - 1
    rest = s % n
    while rest > 0:
        result[index] += 1
        rest -= 1
        index -= 1
        if index < 0:
            index = n - 1
    return result