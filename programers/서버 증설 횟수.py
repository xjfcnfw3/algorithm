def solution(players, m, k):
    answer = 0
    server = []
    for i in range(len(players)):
        player = players[i]
        max_player = (sum((server + [1])[-k:])) * m
        if max_player > player:
            server.append(0)
        else:
            result = (player - max_player) // m + 1
            answer += result
            server.append(result)
    return answer