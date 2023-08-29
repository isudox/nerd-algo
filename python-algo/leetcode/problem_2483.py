"""2483. Minimum Penalty for a Shop
https://leetcode.com/problems/minimum-penalty-for-a-shop/
"""


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        presum0 = [0] * (n + 1)
        presum1 = [0] * (n + 1)
        for i in range(1, n + 1):
            presum0[i] = presum0[i - 1] + (customers[i - 1] == 'N')
            presum1[i] = presum1[i - 1] + (customers[i - 1] == 'Y')
        penalty = n
        ans = 0
        for i in range(n + 1):
            cur = presum0[i] + presum1[-1] - presum1[i]
            if cur < penalty:
                ans = i
                penalty = cur
        return ans
