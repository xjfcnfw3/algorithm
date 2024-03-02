from collections import defaultdict


def solution(genres, plays):
    d = defaultdict(list)
    g = defaultdict(int)
    answer = []
    for i in range(len(genres)):
        d[genres[i]].append([i, plays[i]])
        g[genres[i]] += plays[i]
    g = sorted(g.items(), key=lambda x: x[1], reverse=True)
    for i in g:
        genre = i[0]
        d[genre].sort(reverse=True, key=lambda x: x[1])
        for j in range(len(d[genre])):
            if j >= 2:
                break
            answer.append(d[genre][j][0])

    return answer