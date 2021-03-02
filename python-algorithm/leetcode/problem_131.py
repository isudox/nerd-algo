"""131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(begin: int, end: int) -> bool:
            while begin < end:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True

        def dfs(x: int, store: List[str]):
            if x < n:
                ans.append(store)
            else:
                for i in range(x, n):
                    if is_palindrome(x, i):
                        new_store = store[:]
                        new_store.append(s[x: i + 1])
                        dfs(i + 1, new_store)

        n = len(s)
        ans = []
        dfs(0, [])
        return ans
