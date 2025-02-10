t = int(input())


def bf():
    for i in range(1, n + 1):
        for j in range(len(edges)):
            start, end, cost = edges[j]
            if distance[end] > distance[start] + cost:
                distance[end] = distance[start] + cost
                if i == n:
                    return True
    return False


for _ in range(t):
    n, m, w = map(int, input().split())
    distance = [1e9] * (n + 1)
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])
    if bf():
        print("YES")
    else:
        print("NO")