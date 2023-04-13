"""103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def zigzag_level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        flag = True
        while queue:
            values = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if flag:
                    values.append(node.val)
                else:
                    values.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(values)
            flag = not flag
        return ans
