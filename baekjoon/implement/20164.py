min_result, max_result = 1e9, 0
n = input()


def check_number(number):
    result = 0
    for n in number:
        if int(n) % 2 != 0:
            result += 1
    return result


def check(n, count):
    global min_result, max_result
    count += check_number(n)
    if len(n) == 1:
        if min_result > count:
            min_result = count
        if max_result < count:
            max_result = count
        return
    if len(n) == 2:
        check(str(int(n[0]) + int(n[1])), count)
    elif len(n) >= 3:
        for i in range(1, len(n) - 1):
            for j in range(i + 1, len(n)):
                check(str(int(n[0:i]) + int(n[i:j]) + int(n[j:])), count)


check(n, 0)
print(min_result, max_result)
