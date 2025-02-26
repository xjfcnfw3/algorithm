def search(num, li, n):
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        if li[mid] == num:
            return True
        elif li[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return False


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m = int(input())
    note = list(map(int, input().split()))
    for num in note:
        if search(num, arr, n):
            print(1)
        else:
            print(0)
