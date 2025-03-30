def solution(n, stations, w):
    answer = 0
    width = w * 2 + 1
    start = 1
    for station in stations:
        if station - w - start > 0:
            answer += (station - w - start) // width
            if (station - w - start) % width:
                answer += 1
        start = w + station + 1
    if n - start + 1 > 0:
        answer += (n - start + 1) // width
        if (n - start + 1) % width:
            answer += 1
    return answer