T = 10
for test_case in range(1, T + 1):
    n, t = map(str, input().split())
    t = list(t)
    while True:
        offset = False
        for i in reversed(range(1, len(t))):
            if t[i] == t[i - 1]:
                offset = True
                del t[i]
                del t[i - 1]
                break
        if not offset:
            break
    print("#" + str(test_case) + " ", end = "")
    print("".join(t))