def get_num(row, index):
    result = 0
    for value in row:
        result += value % index
    return result

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : (x[col - 1], -x[0]))
    answer = get_num(data[row_begin - 1], row_begin)
    for i in range(row_begin + 1, row_end + 1):
        answer = answer ^ get_num(data[i - 1], i)
    return answer