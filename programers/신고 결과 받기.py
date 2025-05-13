def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user_report = {}
    user_mail = {}
    user_index = {user: idx for idx, user in enumerate(id_list)}

    for row in report:
        a, b = row.split()
        user_report.setdefault(b, set()).add(a)
        user_mail.setdefault(a, set()).add(b)

    for key in user_report:
        if len(user_report[key]) >= k:
            for id in user_report[key]:
                answer[user_index[id]] += 1

    return answer
