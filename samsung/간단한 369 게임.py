s = {"3", "6", "9"}


def check(num):
    n = str(num)
    result = n
    for i in range(len(n)):
        if n[i] in s:
            if "-" not in result:
                result = "-"
            else:
                result += "-"
    return result


T = int(input())
for test_case in range(1, T + 1):
    print(check(test_case), end=" ")
