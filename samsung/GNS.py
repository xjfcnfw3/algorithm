T = int(input())
values = {
    "ZRO" : 0,
    "ONE" : 1,
    "TWO" : 2,
    "THR" : 3,
    "FOR" : 4,
    "FIV" : 5,
    "SIX" : 6,
    "SVN" : 7,
    "EGT" : 8,
    "NIN" : 9
}
for test_case in range(1, T + 1):
    t, n = input().split()
    arr = list(input().split())
    arr.sort(key=lambda x : values[x])
    print(t)
    print(*arr)
