from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    answer = ""
    for i in range(9, -1, -1):
        i = str(i)
        if i in x and i in y:
            if i == "0" and answer == '':
                answer = "0"
            else:
                answer += "".join([i for _ in range(min(x[i], y[i]))])
    if answer:
        return answer
    return "-1"