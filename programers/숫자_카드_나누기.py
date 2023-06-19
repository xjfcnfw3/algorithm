from functools import reduce
from fractions import gcd


def solution(arrayA, arrayB):
    global answer
    answer = 0

    def find_gcd(array):
        return reduce(gcd, array)

    def get_number_list(array):
        max_number = min(array)
        result = []
        for i in range(2, find_gcd(array) + 1):
            if check_divide(array, i):
                result.append(i)
        return result

    def check_divide(array, num):
        for number in array:
            if number % num != 0:
                return False
        return True

    def check_non_divide(array, num):
        for number in array:
            if number % num == 0:
                return False
        return True

    def check(arrayA, arrayB):
        global answer
        arrayA = set(arrayA)
        arrayB = set(arrayB)
        result_a = get_number_list(arrayA)
        result_b = get_number_list(arrayB)

        for a_num in result_a:
            if check_non_divide(arrayB, a_num):
                answer = max(answer, a_num)

        for b_num in result_b:
            if check_non_divide(arrayA, b_num):
                answer = max(answer, b_num)

    check(arrayA, arrayB)
    return answer