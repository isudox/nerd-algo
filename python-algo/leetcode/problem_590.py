"""590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for node in root.children:
            ans.extend(self.postorder(node))
        ans.append(root.val)
        return ans

    def postorder2(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        q = [(0, root)]  # 0 means the count of visited children of root
        while q:
            cnt, node = q.pop()
            if not node:
                continue
            if cnt == len(node.children):
                ans.append(node.val)
            if cnt < len(node.children):
                q.append((cnt + 1, node))
                q.append((0, node.children[cnt]))
        return ans


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
