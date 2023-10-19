T = int(input())
for test_case in range(1, T + 1):
    s = list(input())
    chars_set = set()
    result = []
    for c in s:
        if c in chars_set:
            chars_set.remove(c)
        else:
            chars_set.add(c)
    result = list(chars_set)
    result.sort()

    if result:
        print("#{} {}".format(test_case, "".join(result)))
    else:
        print("#{} Good".format(test_case))
