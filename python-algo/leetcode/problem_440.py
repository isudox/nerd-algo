"""440. K-th Smallest in Lexicographical Order
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
"""
import collections


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def dfs(t: Trie) -> bool:
            nonlocal k, ans
            found = False
            if k == 0:
                ans = t.val
                return True
            for child in t.children.values():
                k -= 1
                if dfs(child):
                    found = True
                    break
            return found

        trie = Trie(-1)
        for i in range(1, n + 1):
            trie.add(str(i))
        ans = -1
        dfs(trie)
        return ans


class Trie:
    def __init__(self, val: int) -> None:
        self.val = val
        self.children = collections.defaultdict(Trie)

    def add(self, num: str) -> None:
        node = self
        prefix = ''
        for ch in num:
            prefix += ch
            d = int(prefix)
            if d in node.children:
                node = node.children[d]
            else:
                node.children[d] = Trie(d)
                node = node.children[d]
