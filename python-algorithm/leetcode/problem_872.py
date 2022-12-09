"""872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
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
