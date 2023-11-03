T = int(input())
for test_case in range(1, T + 1):
    s = input()
    temp = ""

    for c in s:
        temp += c
        length = len(temp)
        if temp == s[length:length + length]:
            break
    print("#{} {}".format(test_case, len(temp)))