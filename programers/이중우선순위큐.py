import heapq

def solution(operations):
    q = []
    answer = []
    for operation in operations:
        if operation[0] == "I":
            heapq.heappush(q, int(operation[2:]))
        else:
            if not q:
                continue

            if operation[2] == "-":
                heapq.heappop(q)
            else:
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
    if q:
        answer.append(max(q))
        answer.append(min(q))
    else:
        answer.append(0)
        answer.append(0)

    return answer