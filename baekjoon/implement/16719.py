import heapq
s = input()

result = [''] * len(s)

def solution(current, start_index):
    if current == "":
        return

    min_char = min(current)
    min_char_index = list(current).index(min_char)

    result[start_index + min_char_index] = min_char

    print("".join(result))

    solution(current[min_char_index + 1:], start_index + min_char_index + 1)

    solution(current[:min_char_index], start_index)

solution(s, 0)