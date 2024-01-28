def solution(storey):
    answer = 0
    while storey:
        reminder = storey % 10

        if reminder > 5:
            answer += 10 - reminder
            storey += 10
        elif reminder == 5:
            if (storey // 10) % 10 > 4:
                answer += 10 - reminder
                storey += 10
            else:
                answer += reminder
        else:
            answer += reminder
        storey //= 10
    return answer
