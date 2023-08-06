"""95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""
import copy
from typing import List
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def generate_trees_1(self, n: int) -> List[TreeNode]:
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

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(i: int, j: int) -> List[Optional[TreeNode]]:
            if i > j:
                return [None]
            ret = []
            for x in range(i, j + 1):
                left = dfs(i, x - 1)
                right = dfs(x + 1, j)
                for l in left:
                    for r in right:
                        ret.append(TreeNode(x, l, r))
            return ret

        return dfs(1, n)
