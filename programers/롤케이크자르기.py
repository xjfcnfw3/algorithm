from collections import Counter
def solution(topping):
    answer = 0
    d = dict(Counter(topping))
    a = set()
    offset = False
    for i in range(len(topping) - 1):
        d[topping[i]] -= 1
        if d[topping[i]] == 0:
            d.pop(topping[i])
        a.add(topping[i])
        if len(a) == len(d):
            offset = True
            answer += 1
        elif offset:
            break
    return answer