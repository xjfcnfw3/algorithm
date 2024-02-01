from collections import defaultdict
def solution(gems):
    kinds = len(set(gems))
    left, right = 0, len(gems) - 1
    l, r = 0, 0
    current = defaultdict(int)
    current[gems[0]] = 1
    while True:
        if len(current) == kinds:
            if r - l < right - left:
                left, right = l, r
            current[gems[l]] -= 1
            if current[gems[l]] == 0:
                current.pop(gems[l])
            l += 1
        else:
            r += 1
            if r >= len(gems): break
            current[gems[r]] += 1
    return [left+1, right + 1]