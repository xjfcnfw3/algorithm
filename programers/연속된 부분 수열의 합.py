def solution(sequence, k):
    left, right = 0, len(sequence) - 1
    start, end = 0, 0
    s = sequence[0]
    while True:
        if s >= k:
            if s == k:
                if end - start < right - left:
                    left, right = start, end
            s -= sequence[start]
            start += 1
        else:
            end += 1
            if end >= len(sequence) : break
            s += sequence[end]
    answer = [left, right]
    return answer