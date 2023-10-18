T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    days = []
    for i in range(len(arr)):
        if arr[i] == 1:
            days.append(i)
    result = 1e9
    for i in range(len(days)):
        c_result = 0
        day = days[i]
        temp = n
        while temp:
            if day in days:
                temp -= 1
            c_result += 1
            day += 1
            if day == 7:
                day = 0
        result = min(c_result, result)
    print("#{} {}".format(test_case, result))