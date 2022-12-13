# 이 문제는 순열로 풀수 없는 문제다. 입력된 숫자보다 큰 자릿수를 가진 경우를 생각해보자
# 그렇다고 큰 자릿수를 적용하면 0이 고장날 때 최솟값을 구하지 못하는 문제 발생
# ex) 9999을 입력시 10000가 최소인 경우
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

if m:
    broken = set(map(int, input().split(" ")))
else:
    broken = set()

count = abs(100 - n)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in broken:
            break

        elif j == len(i) -1:
            count = min(count, abs(int(i) - n) + len(i))

print(count)