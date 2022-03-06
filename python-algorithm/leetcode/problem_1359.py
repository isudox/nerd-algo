"""1359. Count All Valid Pickup and Delivery Options
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
"""


class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        mode = int(1e9 + 7)
        ans = 1
        for i in range(2, n + 1):
            ans = ans * (2 * i * i - i) % mode
        return ans
