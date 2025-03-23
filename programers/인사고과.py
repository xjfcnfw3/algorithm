def solution(scores):
    target_a, target_b = scores[0]
    point = target_a + target_b
    answer = 1

    max_point = 0

    scores.sort(key=lambda x: (-x[0], x[1]))

    for a, b in scores:
        if target_a < a and target_b < b:
            return -1
        if b >= max_point:
            max_point = b
            if a + b > point:
                answer += 1
    return answer