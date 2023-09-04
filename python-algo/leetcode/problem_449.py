"""449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
"""
from typing import Optional

import common.converter
from common.tree_node import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        ret = str(root.val)
        if root.left:
            ret += ',' + self.serialize(root.left)
        if root.right:
            ret += ',' + self.serialize(root.right)
        return ret

    def deserialize(self, data: str) -> Optional[TreeNode]:
        def helper(i: int, j: int) -> Optional[TreeNode]:
            if i > j:
                return None
            ret = TreeNode(int(nums[i]))
            k = i + 1
            while k <= j and nums[k] < nums[i]:
                k += 1
            ret.left = helper(i + 1, k - 1)
            ret.right = helper(k, j)
            return ret

        if not data:
            return None
        nums = data.split(',')
        return helper(0, len(nums) - 1)
