"""424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can
perform at most k operations on that string.

In one operation, you can choose any character of the string and change it
to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters
you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 10^4.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""


class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n - 1:
            return n
        memo = [0] * 26
        l, r, max_same, ans = 0, 0, 0, 0
        while r < n:
            memo[ord(s[r]) - ord('A')] += 1
            max_same = max(max_same, memo[ord(s[r]) - ord('A')])
            if r - l + 1 - max_same > k:
                memo[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
            ans = max(ans, r - l)
        return ans
