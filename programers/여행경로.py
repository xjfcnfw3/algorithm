from collections import defaultdict

def solution(tickets):
    global answer
    answer = []
    graph = defaultdict(list)
    visited = set()

    for ticket in tickets:
        graph[ticket[0]].append([ticket[1], False])
        graph[ticket[0]].sort()

    def dfs(city, result):
        global answer
        if len(result) == len(tickets) + 1:
            answer = result
            return
        if len(answer) != 0:
            return
        for i in range(len(graph[city])):
            next_city, visited = graph[city][i]
            if not visited:
                graph[city][i][1] = True
                dfs(next_city, result + [next_city])
                graph[city][i][1] = False

    dfs("ICN", ["ICN"])
    return answer