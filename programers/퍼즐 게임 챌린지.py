def solution(diffs, times, limit):
    answer = 1e9
    start, end = min(diffs), max(diffs)
    while start <= end:
        mid = (end + start) // 2
        time = 0
        for i in range(len(diffs)):
            if mid < diffs[i]:
                time += (times[i] + times[i - 1]) * (diffs[i] - mid) + times[i]
            else:
                time += times[i]
        if time <= limit:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
    return answer