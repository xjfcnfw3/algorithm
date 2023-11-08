T = int(input())
z = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        a, b, c = map(int, input().split())
        sum_value = (a * 0.35) + (b * 0.45) + (c * 0.2)
        arr.append(sum_value)
    point = arr[k - 1]
    arr.sort(reverse=True)
    val = n // 10
    index = arr.index(point) // val
    print("#{} {}".format(test_case, z[index]))