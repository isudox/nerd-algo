"""144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def iterative_preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        s = [root]  # FILO stack
        while s:
            node = s.pop()
            ans.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return ans

    def recursive_preorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        ans += self.recursive_preorder_traversal(root.left)
        ans += self.recursive_preorder_traversal(root.right)
        return ans
