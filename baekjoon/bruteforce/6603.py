from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and len(arr) == 1:
        exit()
    result = combinations(arr[1:], 6)
    for i in result:
        print(*i)
    print()
