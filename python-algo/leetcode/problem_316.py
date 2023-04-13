"""316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once
and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Note: This question is the same as No.1081

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

    1 <= s.length <= 10^4
    s consists of lowercase English letters.
"""
import collections


class Solution:
    def remove_duplicate_letters(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            c = s[i]
            if c in stack:
                continue
            while stack and stack[-1] > c and s.find(stack[-1], i) != -1:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = collections.defaultdict(int)
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last_pos:
                last_pos[s[i]] = i
        visited = collections.defaultdict(int)
        stack = []
        for i, ch in enumerate(s):
            if visited[ch]:
                continue
            visited[ch] += 1
            while stack and stack[-1] > ch and last_pos[stack[-1]] > i:
                visited[stack.pop()] -= 1
            stack.append(ch)
        return ''.join(stack)
