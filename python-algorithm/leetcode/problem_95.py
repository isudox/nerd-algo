"""95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, generate all structurally unique BST's (binary search
trees) that store values 1 ... n.

Example:


Input: 3
Output:
[
[1,null,3,2],
[3,2,null,1],
[3,1,null,null,2],
[2,1,3],
[1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

⁠  1         3     3      2      1
⁠   \       /     /      / \      \
⁠    3     2     1      1   3      2
⁠   /     /       \                 \
⁠  2     1         2                 3
"""
import copy
from typing import List

from common.tree_node import TreeNode


class Solution:
    def generate_trees_1(self, n: int) -> List[TreeNode]:
        """
        recursive
        :param n:
        :return:
        """
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]

        def backtrack(left: int, right: int) -> List[TreeNode]:
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            trees = []
            for i in range(left, right + 1):
                for left_tree in backtrack(left, i - 1):
                    for right_tree in backtrack(i + 1, right):
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            return trees

        return backtrack(1, n)

    def generate_trees_2(self, n: int) -> List[TreeNode]:
        """
        dp
        :param n:
        :return:
        """

        def modify_tree(node: TreeNode, offset: int):
            if offset == 0 or not node:
                return
            node.val += offset
            modify_tree(node.left, offset)
            modify_tree(node.right, offset)

        # dp[i] stores the trees of n=i
        if n == 0:
            return []
        dp = [[] for _ in range(n + 2)]
        dp[0].append(None)
        dp[1].append(TreeNode(1))
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                for left_tree in dp[j - 1]:
                    for right_tree in dp[i - j]:
                        root = TreeNode(j)
                        root.left = left_tree
                        new_right_tree = copy.deepcopy(right_tree)
                        modify_tree(new_right_tree, j)
                        root.right = new_right_tree
                        dp[i].append(root)
        return dp[n]
