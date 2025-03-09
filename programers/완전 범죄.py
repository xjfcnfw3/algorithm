def solution(info, n, m):
    d = {0:0}
    for a, b in info:
        temp = {}
        for x, y in d.items():
            if x + a < n and (x + a not in temp or temp[x + a] > y):
                temp[x + a] = y
            if y + b < m and (x not in temp or temp[x] > y + b):
                temp[x] = y + b
        if temp:
            d = temp
        else:
            return -1
    return min(d.keys())