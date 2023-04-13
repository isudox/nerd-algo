"""2034. Stock Price Fluctuation
https://leetcode.com/problems/stock-price-fluctuation/
"""
import bisect


class StockPrice:

    def __init__(self):
        self.cur = -1
        self.time_prices = {}
        self.sort_prices = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.cur:
            self.cur = timestamp
        if timestamp not in self.time_prices:
            self.time_prices[timestamp] = price
            pos = bisect.bisect_left(self.sort_prices, price)
            self.sort_prices.insert(pos, price)
        else:
            pre_price = self.time_prices.pop(timestamp)
            self.sort_prices.remove(pre_price)
            self.update(timestamp, price)

    def current(self) -> int:
        return self.time_prices[self.cur]

    def maximum(self) -> int:
        return self.sort_prices[-1]

    def minimum(self) -> int:
        return self.sort_prices[0]
