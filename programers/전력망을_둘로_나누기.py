from collections import defaultdict, deque


def solution(n, wires):
    tree = defaultdict(list)
    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    def check(wire, start):
        visited = [False] * (n + 1)
        q = deque()
        q.append(start)
        result = 0
        while q:
            node = q.popleft()
            visited[node] = True
            result += 1
            for next_node in tree[node]:
                if node in wire and next_node in wire:
                    continue
                if not visited[next_node]:
                    q.append(next_node)
        return result

    answer = 999999

    for wire in wires:
        result = check(wire, 1)
        answer = min(answer, abs(n - 2 * result))

    return answer