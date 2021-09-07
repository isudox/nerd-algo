"""5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longest_palindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return s[left + 1: right]

        n = len(s)
        max_len = 0
        ans = ''
        for i in range(n):
            odd_str = expand(i, i)
            even_str = expand(i, i + 1)
            if len(odd_str) > max_len:
                max_len = len(odd_str)
                ans = odd_str
            if len(even_str) > max_len:
                max_len = len(even_str)
                ans = even_str
        return ans
