"""1332. Remove Palindromic Subsequences
https://leetcode-cn.com/problems/remove-palindromic-subsequences/
"""


def remove_palindrome_sub(s: str) -> int:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return 2
        i += 1
        j -= 1
    return 1
