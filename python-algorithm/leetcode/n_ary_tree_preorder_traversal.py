"""589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).


Follow up:

Recursive solution is trivial, could you do it iteratively?
"""
from typing import List


class Solution:
    def preorder(self, root) -> List[int]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            node = s.pop()
            ans.append(node.val)
            children = node.children
            if children:
                for i in range(len(children) - 1, -1, -1):
                    s.append(children[i])
        return ans
