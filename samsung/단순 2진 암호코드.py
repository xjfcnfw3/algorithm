answers = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}
T = int(input())

for test_case in range(1, T + 1):
    x, y = map(int, input().split())
    arr = [list(input()) for _ in range(x)]
    complete = False
    answer = ""
    for i in range(x):
        for j in reversed(range(y)):
            if arr[i][j] == "1":
                answer = "".join((arr[i][j - 55:j + 1]))
                complete = True
                break
        if complete:
            break
    result = 0
    result2 = 0
    count = 1
    for i in range(0, len(answer), 7):
        if count % 2 == 0:
            result += answers[answer[i:i + 7]]
        else:
            result += answers[answer[i:i + 7]] * 3
        result2 += answers[answer[i:i + 7]]
        count += 1

    if result % 10 == 0:
        print("#" + str(test_case) + " " + str(result2))
    else:
        print("#" + str(test_case) + " 0")