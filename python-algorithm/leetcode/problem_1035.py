"""1035. Uncrossed Lines
https://leetcode.com/problems/uncrossed-lines/

We write the integers of nums1 and nums2 (in the order they are given) on
two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers
nums1[i] and nums2[j] such that:


nums1[i] == nums2[j];
The line we draw does not intersect any other connecting (non-horizontal)
line.

Note that a connecting lines cannot intersect even at the endpoints: each
number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:

Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1]=4 to
nums2[2]=4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2

Note:

1 <= nums1.length <= 500
1 <= nums2.length <= 500
1 <= nums1[i], nums2[i] <= 2000
"""
from typing import List


class Solution:
    def max_uncrossed_lines(self, nums1: List[int], nums2: List[int]) -> int:
        """DFS, Time Limit Exceeded"""
        def dfs(x: int, y: int) -> int:
            if x == len(nums1) or y == len(nums2):
                return 0
            ret = dfs(x + 1, y)
            for pos in lines[x]:
                if pos >= y:
                    ret = max(ret, dfs(x + 1, pos + 1) + 1)
                    break
            return ret

        lines = [[] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    lines[i].append(j)
        return dfs(0, 0)

    def max_uncrossed_lines2(self, nums1: List[int], nums2: List[int]) -> int:
        """DFS + Memo"""
        def dfs(x: int, y: int) -> int:
            if x == len(nums1) or y == len(nums2):
                return 0
            if memo[x][y] != -1:
                return memo[x][y]
            ret = dfs(x + 1, y)
            for pos in lines[x]:
                if pos >= y:
                    ret = max(ret, dfs(x + 1, pos + 1) + 1)
                    break
            memo[x][y] = ret
            return ret

        lines = [[] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    lines[i].append(j)
        memo = [[-1] * len(nums2) for _ in range(len(nums1))]
        return dfs(0, 0)

    def max_uncrossed_lines3(self, nums1: List[int], nums2: List[int]) -> int:
        """DP"""
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        dp[0][0] = 1 if nums1[0] == nums2[0] else 0
        for i in range(1, len(nums1)):
            dp[i][0] = 1 if nums1[i] == nums2[0] else dp[i - 1][0]
        for j in range(1, len(nums2)):
            dp[0][j] = 1 if nums2[j] == nums1[0] else dp[0][j - 1]
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]
