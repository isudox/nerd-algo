"""140. Word Break II
https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
from typing import List


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> List[str]:
        def dfs(string: str) -> List[str]:
            if string in memo:
                return memo[string]
            cur_ans = []
            if string in word_map:
                cur_ans.append(string)
            for i in range(1, len(string)):
                left, right = string[:i], string[i:]
                if left not in word_map:
                    continue
                for words in dfs(right):
                    cur_sentence = ''
                    for w in words:
                        cur_sentence += w
                    cur_ans.append(left + ' ' + cur_sentence)
            memo[string] = cur_ans
            return memo[string]

        memo = {}
        word_map = {}
        for word in word_dict:
            word_map[word] = True
        return dfs(s)
