"""1269. Number of Ways to Stay in the Same Place After Some Steps
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

You have a pointer at index 0 in an array of size arrLen. At each step, you
can move 1 position to the left, 1 position to the right in the array or stay
in the same place (The pointer should not be placed outside the array at any
time).

Given two integers steps and arrLen, return the number of ways such that your
pointer still at index 0 after exactly steps steps.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 different ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay

Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 different ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay

Example 3:

Input: steps = 4, arrLen = 2
Output: 8

Constraints:

1 <= steps <= 500
1 <= arrLen <= 10^6
"""


class Solution:
    def num_ways(self, steps: int, arr_len: int) -> int:
        base = 1000000007
        dp, next_dp = [1], []
        for i in range(1, steps + 1):
            for j in range(min(i + 1, arr_len)):
                cur = 0
                if j <= i - 1:
                    cur = dp[j]
                if j - 1 >= 0:
                    cur = (cur + dp[j - 1]) % base
                if j + 1 <= i - 1 and j + 1 <= arr_len - 1:
                    cur = (cur + dp[j + 1]) % base
                if i == steps:
                    return cur
                next_dp.append(cur)
            dp = next_dp
            next_dp = []
        return dp[0]
