def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        day = startday
        time = schedules[i] + 10
        offset = True
        if time % 100 >= 60:
            time += 100
            time -= 60

        for j in range(len(timelogs[i])):
            if day == 6 or day == 7:
                day = day + 1 if day < 7 else 1
                continue
            if timelogs[i][j] > time:
                offset = False
                break
            day = day + 1 if day < 7 else 1
        if offset:
            answer += 1
    return answer