def solution(routes):
    routes.sort(key=lambda x : (x[1], x[0]))
    answer = 1
    current = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > current:
            answer += 1
            current = routes[i][1]
    return answer