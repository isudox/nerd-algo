"""998. Maximum Binary Tree II
https://leetcode.com/problems/maximum-binary-tree-ii/
"""
from typing import Optional
from typing import List
from common.tree_node import TreeNode


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            l_nodes, r_nodes = traversal(node.left), traversal(node.right)
            return l_nodes + [node.val] + r_nodes

        def construct(nums: List[int], l: int, r: int) -> TreeNode:
            if l >= r:
                return None
            pos, maxx = -1, -1
            for i in range(l, r):
                if nums[i] > maxx:
                    maxx = nums[i]
                    pos = i
            ret = TreeNode(nums[pos])
            ret.left = construct(nums, l, pos)
            ret.right = construct(nums, pos + 1, r)
            return ret

        nodes = traversal(root)
        nodes.append(val)
        return construct(nodes, 0, len(nodes))
