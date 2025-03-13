def solution(targets):
    targets.sort(key=lambda x: x[1])
    end = targets[0][1]
    answer = 1
    for i in range(1, len(targets)):
        if targets[i][0] >= end:
            end = targets[i][1]
            answer += 1
    return answer