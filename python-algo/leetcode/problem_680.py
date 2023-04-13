"""680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(i: int, j: int, flag: bool) -> bool:
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                elif not flag:
                    return False
                else:
                    return helper(i + 1, j, False) or helper(i, j - 1, False)
            return True

        return helper(0, len(s) - 1, True)
