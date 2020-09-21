"""538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/

Given a Binary Search Tree (BST), convert it to a Greater Tree such that
every key of the original BST is changed to the original key plus sum of
all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038:
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""
from common.tree_node import TreeNode


class Solution:
    def convert_bst(self, root: TreeNode) -> TreeNode:
        seq_node, seq_val, stack = [], [], []
        # in-order traversal.
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                seq_node.append(node)
                seq_val.append(node.val)
                p = node.right
        for i in range(len(seq_val) - 1):
            seq_node[i].val = sum(seq_val[i:])
        return root

    def convert_bst_1(self, root: TreeNode) -> TreeNode:
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

    def convert_bst_2(self, root: TreeNode) -> TreeNode:
        pass
