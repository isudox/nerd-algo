"""524. Longest Word in Dictionary through Deleting
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""
import bisect
from typing import List


class Solution:
    def find_longest_word(self, s: str, dictionary: List[str]) -> str:
        mapper = [[] for _ in range(26)]
        for i, c in enumerate(s):
            mapper[ord(c) - 97].append(i)
        dictionary.sort(key=lambda x: len(x), reverse=True)
        ans = ''
        for word in dictionary:
            if len(word) < len(ans):
                break
            i, j = 0, len(word) - 1
            left, right = -1, len(s)
            while i < j:
                pi = mapper[ord(word[i]) - 97]
                pj = mapper[ord(word[j]) - 97]
                if not pi or not pj:
                    break
                pos = bisect.bisect_right(pi, left)
                if pos == len(pi):
                    break
                left = pi[pos]
                pos = bisect.bisect_left(pj, right) - 1
                if pos < 0:
                    break
                right = pj[pos]
                if left >= right:
                    break
                i += 1
                j -= 1
            if i >= j:
                if not ans or word < ans:
                    ans = word
        return ans
