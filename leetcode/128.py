import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = sys.maxsize
        profit = -sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit