"""890.
"""
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def valid(w: str, p: str) -> bool:
            if len(w) != len(p):
                return False
            store1, store2 = dict(), dict()
            for i in range(len(w)):
                if p[i] in store1:
                    if store1[p[i]] != w[i]:
                        return False
                else:
                    store1[p[i]] = w[i]
                if w[i] in store2:
                    if store2[w[i]] != p[i]:
                        return False
                else:
                    store2[w[i]] = p[i]
            return True

        ans = []
        for word in words:
            if valid(word, pattern):
                ans.append(word)
        return ans
