n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

trust_mans = list(map(int, input().split()))[1:]


def find(a):
    if a != parents[a]:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root in trust_mans and b_root in trust_mans:
        return

    if a_root in trust_mans:
        parents[b_root] = a_root
    elif b_root in trust_mans:
        parents[a_root] = b_root
    else:
        if a_root < b_root:
            parents[b_root] = a_root
        else:
            parents[a_root] = b_root


parties = []

for _ in range(m):
    peoples = list(map(int, input().split()))[1:]
    offset = False
    for i in range(len(peoples) - 1):
        union(peoples[i], peoples[i + 1])
    parties.append(peoples)

result = len(parties)

for party in parties:
    for people in party:
        if find(people) in trust_mans:
            result -= 1
            break

print(result)
