"""1110. Delete Nodes And Return Forest
https://leetcode.com/problems/delete-nodes-and-return-forest/
"""
from typing import List, Optional

from common.tree_node import TreeNode


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            node.left = helper(node.left)
            node.right = helper(node.right)
            if node.val not in del_nodes:
                return node
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            return None

        ans = []
        del_nodes = set(to_delete)
        if helper(root):
            ans.append(root)
        return ans
