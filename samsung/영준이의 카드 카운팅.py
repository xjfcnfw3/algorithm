T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(input())
    arr = [arr[i*3:i*3+3] for i in range(len(arr)//3)]
    s, d, h, c = set(), set(), set(), set()
    result = True
    for card in arr:
        shape = card[0]
        num = int("".join(card[1:]))
        if shape == "S":
            if num in s:
                result = False
                break
            else:
                s.add(num)
        elif shape == "D":
            if num in d:
                result = False
                break
            else:
                d.add(num)
        elif shape == "H":
            if num in h:
                result = False
                break
            else:
                h.add(num)
        elif shape == "C":
            if num in c:
                result = False
                break
            else:
                c.add(num)
    if result:
        print("#{} {} {} {} {}".format(test_case, 13-len(s), 13-len(d), 13-len(h), 13-len(c)))
    else:
        print("#{} ERROR".format(test_case))