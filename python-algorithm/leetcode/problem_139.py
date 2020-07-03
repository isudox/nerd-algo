"""139. Word Break
https://leetcode.com/problems/word-break/description/

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:


The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.


Example 1:


Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet
code".


Example 2:


Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple
pen apple".
Note that you are allowed to reuse a dictionary word.


Example 3:


Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from typing import List


class Solution:

    def word_break_1(self, s: str, word_dict: List[str]) -> bool:
        unmatched = set()

        def backtrack(string: str) -> bool:
            if string in unmatched:
                return False
            for word in word_dict:
                if string == word:
                    return True
                if string.startswith(word):
                    if backtrack(string[len(word):]):
                        return True
            unmatched.add(string)
            return False

        return backtrack(s)

    def word_break_2(self, s: str, word_dict: List[str]) -> bool:
        visited = {}

        def backtrack(cur_str: str) -> bool:
            if cur_str in visited:
                return visited[cur_str]
            if cur_str in word_dict:
                return True
            for i in range(1, len(cur_str)):
                if cur_str[:i] in word_dict and backtrack(cur_str[i:]):
                    visited[cur_str] = True
                    return True
                i += 1
            visited[cur_str] = False
            return False

        return backtrack(s)
