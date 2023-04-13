"""541. Reverse String II
https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    def reverse_str(self, s: str, k: int) -> str:
        n = k * 2
        ans = list(s)
        for i in range(len(s) // n + 1):
            l = n * i
            r = min(l + k - 1, len(s) - 1)
            while l < r:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
        return ''.join(ans)
