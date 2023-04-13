"""522. Longest Uncommon Subsequence II
https://leetcode.com/problems/longest-uncommon-subsequence-ii/
"""
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(a: str, b: str) -> bool:
            # check if a is subsequence of b
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        ans = -1
        for i in range(len(strs)):
            flag = True
            for j in range(len(strs)):
                if i == j:
                    continue
                if check(strs[i], strs[j]):
                    flag = False
                    break
            if flag:
                ans = max(ans, len(strs[i]))
        return ans

