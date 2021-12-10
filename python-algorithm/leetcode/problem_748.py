"""748. Shortest Completing Word
https://leetcode.com/problems/shortest-completing-word/
"""
import collections


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = [0] * 26
        for ch in licensePlate:
            x = ord(ch)
            if 97 <= x <= 122:
                letters[x - 97] += 1
            if 65 <= x <= 90:
                letters[x - 65] += 1
        ans = ' ' * 16
        for word in words:
            skipped = False
            counter = collections.Counter(word)
            for i, cnt in enumerate(letters):
                if counter[chr(i + 97)] < cnt:
                    skipped = True
                    break
            if skipped:
                continue
            else:
                if len(word) < len(ans):
                    ans = word
        return ans
