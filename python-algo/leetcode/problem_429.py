"""429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def level_order(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            cur = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                cur.append(node.val)
                if node.children:
                    for child in node.children:
                        q.append(child)
            ans.append(cur)
        return ans
