"""116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children.
The binary tree has the following definition:

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not
count as extra space for this problem.

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""
from typing import List


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def recur(node: Node) -> None:
            if not node:
                return
            if node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
            recur(node.left)
            recur(node.right)

        recur(root)
        return root


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
