T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    a_set = set(input().split())
    b_set = set(input().split())
    print("#{} {}".format(test_case, len(a_set & b_set)))