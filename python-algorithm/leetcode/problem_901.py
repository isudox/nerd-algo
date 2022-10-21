"""901. Online Stock Span
https://leetcode.com/problems/online-stock-span/
"""


class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.spanners = []

    def next(self, price: int) -> int:
        cnt = 1
        if self.stocks and self.stocks[-1] <= price:
            i = len(self.stocks) - 1
            while i >= 0:
                if self.stocks[i] > price:
                    break
                cnt += self.spanners[i]
                i -= self.spanners[i]
        self.stocks.append(price)
        self.spanners.append(cnt)
        return cnt
