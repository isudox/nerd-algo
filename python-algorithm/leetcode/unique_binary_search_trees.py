"""96. Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/description/

Given n, how many structurally unique BST's (binary search trees) that store
values 1 ... n?

Example:


Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

⁠  1         3     3      2      1
⁠   \       /     /      / \      \
⁠    3     2     1      1   3      2
⁠   /     /       \                 \
⁠  2     1         2                 3
"""


class Solution:
    def num_trees_1(self, n: int) -> int:
        if n <= 1:
            return 1
        ans = 0
        for i in range(1, n + 1):
            ans += self.num_trees_1(i - 1) * self.num_trees_1(n - i)
        return ans

    def num_trees_2(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
