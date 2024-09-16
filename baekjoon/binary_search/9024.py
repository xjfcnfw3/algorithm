import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    answer = 0
    temp = 1e9
    for i in range(n):
        left, right = i + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            sum_number = arr[i] + arr[mid]
            if arr[mid] > k - arr[i]:
                right = mid - 1
            else:
                left = mid + 1
            if abs(k - sum_number) < temp:
                answer = 1
                temp = abs(k - sum_number)
            elif abs(k - sum_number) == temp:
                answer += 1
    print(answer)