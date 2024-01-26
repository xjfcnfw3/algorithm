from collections import deque


def solution(order):
    boxes = deque()
    q = deque()
    stk = []
    for i in range(1, len(order) + 1):
        boxes.append(i)
        q.append(order[i - 1])
    while boxes:
        box = boxes.popleft()

        if box == q[0]:
            q.popleft()
        else:
            while stk:
                if stk[-1] == q[0]:
                    q.popleft()
                    stk.pop()
                else:
                    break
            stk.append(box)
    while stk:
        num = stk.pop()
        if q and num == q[0]:
            q.popleft()
        else:
            break
    return len(order) - len(q)