"""872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree, from left to right order, the
values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
8).

Two binary trees are considered leaf-similar if their leaf value sequence is
the same.

Return true if and only if the two given trees with head nodes root1 and
root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1], root2 = [1]
Output: true

Example 3:

Input: root1 = [1], root2 = [2]
Output: false

Example 4:

Input: root1 = [1,2], root2 = [2,2]
Output: true

Example 5:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def leaf_similar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node: TreeNode, leaf: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                leaf.append(node.val)
                return
            helper(node.left, leaf)
            helper(node.right, leaf)

        leaf1, leaf2 = [], []
        helper(root1, leaf1)
        helper(root2, leaf2)
        return leaf1 == leaf2

    def leaf_similar2(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node: TreeNode, leaf: List[int]):
            stack = []
            while node or stack:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if not node.left and not node.right:
                        leaf.append(node.val)
                    node = node.right

        leaf1, leaf2 = [], []
        helper(root1, leaf1)
        helper(root2, leaf2)
        return leaf1 == leaf2

    def leaf_similar3(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node: TreeNode) -> List[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return helper(node.left) + helper(node.right)

        return helper(root1) == helper(root2)

    def leaf_similar4(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(nodes: List[TreeNode]) -> int:
            while True:
                node = nodes.pop()
                if node.right:
                    nodes.append(node.right)
                if node.left:
                    nodes.append(node.left)
                if not node.left and not node.right:
                    return node.val

        s1, s2 = [root1], [root2]
        while s1 and s2:
            if helper(s1) != helper(s2):
                return False
        return not s1 and not s2

    def leaf_similar5(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(node: TreeNode):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from helper(node.left)
                yield from helper(node.right)

        return list(helper(root1)) == list(helper(root2))
