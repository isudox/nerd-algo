"""1281. Subtract the Product and Sum of Digits of an Integer
https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ, mult = 0, 1
        while n:
            n, m = divmod(n, 10)
            summ += m
            mult *= m
        return mult - summ