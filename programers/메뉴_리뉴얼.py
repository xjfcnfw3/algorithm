from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    result = []

    def get_candidate(orders, course):
        candidate = defaultdict(set)
        for i in course:
            for j in range(len(orders)):
                for c in combinations(orders[j], r=i):
                    candidate[len(c)].add("".join(sorted(c)))
        return candidate

    candidate = get_candidate(orders, course)

    def check(candidate, orders):
        result = 0
        candidate = list(candidate)
        for order in orders:
            isIn = True
            for ch in candidate:
                if ch not in order:
                    isIn = False
                    break
            if isIn:
                result += 1
        return result

    for c, li in candidate.items():
        arr = []
        max_count = 0
        for order_candidate in li:
            num = check(order_candidate, orders)
            if num == max_count:
                arr.append(order_candidate)
            elif num > max_count and num > 1:
                arr = [order_candidate]
                max_count = num
        result += arr
    return sorted(result)