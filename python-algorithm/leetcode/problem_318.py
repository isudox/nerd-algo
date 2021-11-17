"""318. Maximum Product of Word Lengths
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""
from typing import List


class Solution:
    def max_product(self, words: List[str]) -> int:
        def has_common(ws1, ws2) -> bool:
            if len(ws1) > len(ws2):
                return has_common(ws2, ws1)
            for ch in ws1:
                if ch in ws2:
                    return True
            return False

        ans = 0
        words_set = []
        for word in words:
            words_set.append(set(word))
        for i in range(len(words_set)):
            for j in range(i + 1, len(words_set)):
                if not has_common(words_set[i], words_set[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
