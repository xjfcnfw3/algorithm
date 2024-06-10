def solution(c):
    c = list(c)
    i, j = len(c) - 2, len(c) - 1
    while i >= 0 and c[i] >= c[i + 1]:
        i -= 1
    if i == -1:
        return False
    while c[i] >= c[j]:
        j -= 1
    c[i], c[j] = c[j], c[i]
    result = c[:i + 1]
    result.extend(list(reversed(c[i + 1:])))

    return result


for _ in range(int(input())):
    c = input()
    result = solution(c)
    if result:
        print(''.join(result))
    else:
        print(c)

