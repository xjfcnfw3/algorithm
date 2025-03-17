def find(num):
    if num == 1:
        return 0
    temp = []
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            if num // i > 10**7:
                temp.append(i)
                continue
            return num // i
    if temp:
        return max(temp)
    return 1

def solution(begin, end):
    answer = [0] * (end - begin + 1)
    for i in range(begin, end + 1):
        answer[i - begin] = find(i)
    return answer