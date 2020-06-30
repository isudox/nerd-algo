"""647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings
in this string.

The substrings with different start indexes or end indexes are counted
as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
"""


class Solution:
    def count_substrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        n = len(s)
        ans = 0
        for i in range(n):
            ans += 1 + expand(i - 1, i + 1) + expand(i, i + 1)
        return ans

    def count_substrings_2(self, s: str) -> int:
        """
        brute force with memo.
        """

        def is_palindromic(i: int, j: int) -> bool:
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        ans = 0
        checked = {}
        for i in range(n):
            for j in range(i, n):
                if s[i: j + 1] in checked:
                    ans += 1
                elif is_palindromic(i, j):
                    ans += 1
                    checked[s[i:j + 1]] = True
        return ans

    def count_substrings_1(self, s: str) -> int:
        """
        brute force
        time complexity: O(N^2)
        space complexity: O(1)
        """

        def is_palindromic(i: int, j: int) -> bool:
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if is_palindromic(i, j):
                    ans += 1
        return ans
