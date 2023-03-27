from collections import deque
def solution(msg):
    answer = []
    q = deque(msg)
    dic = {}
    temp = ""
    for i in range(26):
        dic[chr(ord('a') + i)] = i + 1
    while q:
        temp += q.popleft().lower()
        if temp in dic:
            if q and temp + q[0].lower() not in dic:
                answer.append(dic[temp])
                dic[temp + q[0].lower()] = len(dic) + 1
                temp = ""
            elif not q:
                answer.append(dic[temp])
                temp = ""
    return answer