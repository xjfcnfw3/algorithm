def solution(str1, str2):
    def makelist(input_str):
        s = []
        temp = ""
        for i in range(len(input_str)):
            if ord('a') <= ord(input_str[i]) <= ord('z') or ord('A') <= ord(input_str[i]) <= ord('Z'):
                temp += input_str[i].lower()
                if len(temp) == 2:
                    s.append(temp)
                    temp = input_str[i].lower()
            else:
                temp = ""
        return s
    answer = 0
    a = makelist(str1)
    b = makelist(str2)
    if not a and not b:
        return 65536
    elif not a or not b:
        return 0
    t = []
    for element in a:
        if element in b:
            t.append(element)
            b.remove(element)
    return int(len(t) / (len(a) + len(b)) * 65536)