def solution(numbers):
    arr = [str(number) for number in numbers]
    arr.sort(key = lambda x : x*3, reverse = True)
    return str(int("".join(arr)))