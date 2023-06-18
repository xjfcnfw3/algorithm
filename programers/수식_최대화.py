from itertools import permutations


def solution(expression):
    orders = permutations(("+", "-", "*"), r=3)

    def get_numbers_and_operations(expression):
        operations = []

        numbers = ""
        for i in range(len(expression)):
            if expression[i] == "*" or expression[i] == "+" or expression[i] == "-":
                operations.append(expression[i])
                numbers += " "
            else:
                numbers += expression[i]
        return [operations, list(map(int, numbers.split()))]

    def operate(operation, a, b):
        if operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        return a + b

    def get_result(order, operations_arg, numbers_arg):
        operations = operations_arg[:]
        numbers = numbers_arg[:]
        next_operations = []
        next_numbers = []

        for operation in order:
            for i in range(len(operations)):
                if operations[i] == operation:
                    numbers[i + 1] = operate(operations[i], numbers[i], numbers[i + 1])
                else:
                    next_operations.append(operations[i])
                    next_numbers.append(numbers[i])
            next_numbers.append(numbers[-1])

            numbers = next_numbers
            operations = next_operations
            next_numbers = []
            next_operations = []
        return numbers[0]

    operations, numbers = get_numbers_and_operations(expression)
    answer = 0

    for order in orders:
        answer = max(answer, abs(get_result(order, operations, numbers)))

    return answer