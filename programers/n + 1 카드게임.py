from collections import deque


def check(deck1, deck2, target):
    for card in deck1:
        if target - card in deck2:
            deck1.remove(card)
            deck2.remove(target - card)
            return True
    return False


def solution(coin, cards):
    answer = 1
    hand = cards[:len(cards) // 3]
    deck = deque(cards[len(cards) // 3:])
    target = len(cards) + 1
    pending = []
    while coin >= 0 and deck:
        pending.append(deck.popleft())
        pending.append(deck.popleft())

        if check(hand, hand, target):
            pass
        elif coin >= 1 and check(hand, pending, target):
            coin -= 1
        elif coin >= 2 and check(pending, pending, target):
            coin -= 2
        else:
            break
        answer += 1

    return answer