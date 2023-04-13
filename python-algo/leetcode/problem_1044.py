"""1044. Longest Duplicate Substring
https://leetcode.com/problems/longest-duplicate-substring/
"""


class Solution:
    def longest_dup_substring(self, s: str) -> str:
        def is_dup(x: int) -> tuple:
            seen = {}
            for i in range(n - x + 1):
                sub_str = s[i:i + x]
                if sub_str in seen:
                    return True, sub_str
                seen[sub_str] = True
            return False, ""

        n = len(s)
        i, j = 1, n
        ans = ''
        while i <= j:
            mid = (i + j) // 2
            ok, ret = is_dup(mid)
            if ok:
                ans = ret
                i = mid + 1
            else:
                j = mid
        return ans
