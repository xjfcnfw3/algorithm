def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n + 1)]
    while n != 0:
        fac = factorial(n - 1)
        idx = k // fac
        k = k % fac
        if k == 0:
            answer.append(arr.pop(idx - 1))
        else:
            answer.append(arr.pop(idx))
        n -= 1
    return answer