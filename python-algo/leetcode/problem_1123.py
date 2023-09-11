"""
"""
from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = [root]
        while q:

