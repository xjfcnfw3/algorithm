from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque((v, i) for i, v in enumerate(priorities))
    while q:
        arr = q.popleft()
        if q and max(q)[0] > arr[0]:
            q.append(arr)
        else:
            answer += 1
            if arr[1] == location:
                break
    return answer