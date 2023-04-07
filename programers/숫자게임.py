from collections import deque
def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    answer = 0
    for a in A:
        if a >= B[0]:
            continue
        answer += 1
        del B[0]
    return answer