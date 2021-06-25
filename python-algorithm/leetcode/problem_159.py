"""159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
"""

import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        i = 0
        mark = collections.defaultdict(int)
        first = second = s[0]
        while i < len(s):
            if s[i] in mark:
                i += 1
            elif len(mark) < 2:
                mark[s[i]] = i
                second = s[i]
                i += 1
            else:
                ans = max(ans, i - mark[first])
                del mark[first]
                first = second
                i = mark[first]
        return max(ans, len(s) - mark[first])

