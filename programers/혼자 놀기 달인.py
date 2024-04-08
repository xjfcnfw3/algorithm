def solution(cards):
    answer = 0
    path = []
    for i in range(len(cards)):
        visited = [False] * len(cards)
        arr = []
        n = i + 1
        num = 0
        while not visited[n - 1]:
            visited[n - 1] = True
            arr.append(n)
            num += 1
            n = cards[n - 1]
        path.append(arr)

    for j in range(len(cards)):
        max_value = len(path[j]) * (len(cards) - len(path[j]))
        if max_value < answer:
            continue
        for k in range(len(cards)):
            visited = [False] * len(cards)
            n = k + 1
            num = 0
            while not visited[n - 1] and n not in path[j]:
                visited[n - 1] = True
                num += 1
                n = cards[n - 1]
            answer = max(answer, len(path[j]) * num)

    return answer