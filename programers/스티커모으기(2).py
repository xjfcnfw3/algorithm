def solution(sticker):
    if len(sticker) == 1:
        return sticker[-1]

    dp1 = [0] + sticker[:-1]

    for i in range(2, len(dp1)):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    dp2 = [0] + sticker[1:]

    for i in range(2, len(dp2)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    return max(dp1[-1], dp2[-1])