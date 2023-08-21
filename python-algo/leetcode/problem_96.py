"""96. Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/
"""


class Solution:
    def num_trees_1(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

    def num_trees_2(self, n: int) -> int:
        # not accepted
        if n <= 1:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += self.num_trees_2(i - 1) * self.num_trees_2(n - i)

        return ans
