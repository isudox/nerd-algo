"""2490. Circular Sentence
https://leetcode.com/problems/circular-sentence/
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        n = len(words)
        for i in range(n):
            cur, nxt = words[i], words[(i + 1) % n]
            if cur[-1] != nxt[0]:
                return False
        return True
