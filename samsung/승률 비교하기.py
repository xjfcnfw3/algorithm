T = int(input())
result = []

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    if arr[0] / arr[1] == arr[2] / arr[3]:
        result.append("DRAW")
    elif arr[0] / arr[1] > arr[2] / arr[3]:
        result.append("ALICE")
    else:
        result.append("BOB")
for i in range(T):
    print("#{} {}".format(i + 1, result[i]))