T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 1e9
    left, right = 0, 0
    while right < n:
        if right - left < k - 1:
            right += 1
        else:
            answer = min(answer, arr[right] - arr[left])
            left += 1
    print("#{} {}".format(test_case, answer))