import math
def solution(w,h):
    num = math.gcd(w, h)
    return w * h - num * ((w // num) + (h // num) - 1)