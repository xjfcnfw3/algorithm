def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    stack = []
    for i in reversed(range(len(numbers))):
        if i == len(numbers) - 1:
            stack.append(numbers[i])
            continue
        if stack:
            while stack:
                if stack[-1] > numbers[i]:
                    answer[i] = stack[-1]
                    stack.append(numbers[i])
                    break
                stack.pop()
            stack.append(numbers[i])
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = -1
    return answer