"""1813. Sentence Similarity III
https://leetcode.cn/problems/sentence-similarity-iii/
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        words1, words2 = sentence1.split(' '), sentence2.split(' ')
        if len(words1) > len(words2):
            return self.areSentencesSimilar(sentence2, sentence1)
        i1, j1 = 0, len(words1) - 1
        i2, j2 = 0, len(words2) - 1
        while i1 <= j1:
            if words1[i1] != words2[i2] and words1[j1] != words2[j2]:
                return False
            if words1[i1] == words2[i2]:
                i1 += 1
                i2 += 1
            elif words1[j1] == words2[j2]:
                j1 -= 1
                j2 -= 1
        return True
