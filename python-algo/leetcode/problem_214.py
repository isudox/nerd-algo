"""214. Shortest Palindrome
https://leetcode.com/problems/shortest-palindrome/

Given a string s, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can
find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


class Solution:
    def shortest_palindrome(self, s: str) -> str:
        reversed_s = s[::-1]
        n = len(s)
        overlap = 0
        while overlap < n:
            if reversed_s[overlap:] == s[:n - overlap]:
                break
            else:
                overlap += 1
        return reversed_s[:overlap] + s
