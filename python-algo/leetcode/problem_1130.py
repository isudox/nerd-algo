"""1130. Minimum Cost Tree From Leaf Values
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

Given an array arr of positive integers, consider all binary trees such
that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order
traversal of the tree. (Recall that a node is a leaf if and only if it has 0
children.)
The value of each non-leaf node is equal to the product of the largest leaf
value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum
of the values of each non-leaf node. It is guaranteed this sum fits into a
32-bit integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the
second has non-leaf node sum 32.

⁠   24            24
⁠  /  \          /  \
⁠ 12   4        6    8
⁠/  \               / \
6    2             2   4

Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is
less than 2^31).
"""
from typing import List


class Solution:
    def mct_from_leaf_values(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[i][j]: min sum of non-leaf nodes from subtree formed with arr[i] to arr[j]
        dp = [[2147483647] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        # max[i][j]: the max value of subtree leaf nodes formed with arr[i] to arr[j]
        max_nums = [[0] * n for _ in range(n)]
        for r in range(n):
            for l in range(r, -1, -1):
                if l == r:
                    max_nums[l][r] = arr[r]
                else:
                    max_nums[l][r] = max(max_nums[l + 1][r], arr[l])
        for r in range(n):
            for l in range(r, -1, -1):
                for k in range(l, r):
                    val = max_nums[l][k] * max_nums[k + 1][r]
                    dp[l][r] = min(dp[l][r], val + dp[l][k] + dp[k + 1][r])
        return dp[0][-1]
