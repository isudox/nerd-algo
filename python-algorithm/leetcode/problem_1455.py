"""1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i
        return -1
