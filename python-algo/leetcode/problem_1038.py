"""1038. Binary Search Tree to Greater Sum Tree
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        p = root
        stack, node_seq = [], []
        # reversed in-order traversal.
        while p or stack:
            if p:
                stack.append(p)
                p = p.right
            else:
                node = stack.pop()
                node_seq.append(node)
                p = node.left
        pre_sum = 0
        for node in node_seq:
            pre_sum += node.val
            node.val = pre_sum
        return root
