def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]

    discount_emoticons = []

    def make_discount_emoticons(temp, depth):
        if depth == len(temp):
            discount_emoticons.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            make_discount_emoticons(temp, depth + 1)
            temp[depth] -= d

    make_discount_emoticons([0] * len(emoticons), 0)

    for d in range(len(discount_emoticons)):
        join, price = 0, [0] * len(users)
        for e in range(len(emoticons)):
            for u in range(len(users)):
                if users[u][0] <= discount_emoticons[d][e]:
                    price[u] += emoticons[e] * (100 - discount_emoticons[d][e]) / 100

        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0

        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join

    return answer