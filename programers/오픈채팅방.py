def solution(record):
    users = {}
    note = []
    for r in record:
        arr = r.split()
        if len(arr) == 2:
            note.append([2, arr[1]])
        else:
            if arr[0] == "Enter":
                users[arr[1]] = arr[2]
                note.append([1, arr[1]])
            else:
                users[arr[1]] = arr[2]
                note.append([0, arr[1]])
    answer = []
    for n in note:
        if n[0] == 0:
            continue
        if n[0] == 1:
            answer.append(users[n[1]] + "님이 들어왔습니다.")
        else:
            answer.append(users[n[1]] + "님이 나갔습니다.")
    return answer