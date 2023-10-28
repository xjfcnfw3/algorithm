def draw(start, end, num):
    if start > end:
        return
    elif start == end:
        arr[start][start] = num
        return

    for i in range(start, end + 1):
        arr[start][i] = num
        num += 1
    for i in range(start + 1, end + 1):
        arr[i][end] = num
        num += 1
    for i in reversed(range(start, end)):
        arr[end][i] = num
        num += 1
    for i in reversed(range(start + 1, end)):
        arr[i][start] = num
        num += 1
    draw(start + 1, end - 1, num)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    draw(0, len(arr) - 1, 1)
    print(arr)