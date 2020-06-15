"""14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        limit = len(strs[0])
        for s in strs:
            limit = min(len(s), limit)
        for i in range(limit):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    # find the different letter
                    return strs[0][:i]
        return strs[0][:limit]
