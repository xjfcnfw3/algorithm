def solution(expressions):
    def get_num(num, x):

        result = 0

        if num == "0":
            return result

        for i in reversed(range(len(num))):
            result += x ** (len(num) - i - 1) * int(num[i])
        return result

    def get_result(num, x):
        if num == 0:
            return "0"
        result = []
        while num:
            result.append(str(num % x))
            num //= x

        return "".join(result[::-1])

    def split_data(expressions):
        miss, exp, = [], []
        max_num = 0
        for expression in expressions:
            a, op, b, none, result = expression.split()
            if result != "X":
                for n in result:
                    max_num = max(int(n), max_num)
            for n in a:
                max_num = max(int(n), max_num)
            for n in b:
                max_num = max(int(n), max_num)

            if result == "X":
                miss.append([a, op, b, result])
            else:
                exp.append([a, op, b, result])
        return miss, exp, max_num

    answer = []
    miss, exps, max_num = split_data(expressions)
    max_num = max(1, max_num)

    numbers = [i for i in range(max_num + 1, 10)]
    temp = []

    for number in numbers:
        offset = True
        for a, op, b, result in exps:
            a, b, result = get_num(a, number), get_num(b, number), get_num(result, number)
            if op == "+" and a + b != result:
                offset = False
                break
            elif op == "-" and a - b != result:
                offset = False
                break
        if offset:
            temp.append(number)
    numbers = temp

    for number in numbers:
        for i in range(len(miss)):
            a, op, b, result = miss[i]
            a, b = get_num(a, number), get_num(b, number)
            new_result = ""
            if op == "+":
                new_result = get_result(int(a) + int(b), number)
            else:
                new_result = get_result(int(a) - int(b), number)
            if result == "X":
                miss[i][3] = new_result
            elif result != "?" and new_result != result:
                miss[i][3] = "?"
    answer = []
    for row in miss:
        answer.append(row[0] + " " + row[1] + " " + row[2] + " = " + row[3])
    return answer