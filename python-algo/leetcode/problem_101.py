"""101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/description/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

⁠   1
⁠  / \
⁠ 2   2
⁠/ \ / \
3  4 4  3

3241423

But the following [1,2,2,null,3,null,3] is not:

⁠   1
⁠  / \
⁠ 2   2
⁠  \   \
⁠  3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
from common.tree_node import TreeNode


class Solution:
    def is_symmetric_iterative(self, root: TreeNode) -> bool:
        def check(node_1: TreeNode, node_2: TreeNode) -> bool:
            if not node_1 and not node_2:
                return True
            if not (node_1 and node_2):
                return False
            if node_1.val != node_2.val:
                return False
            return True

        if not root:
            return True
        queue = [root]
        while queue:
            i, j = 0, len(queue) - 1
            while i < j:
                if not check(queue[i], queue[j]):
                    return False
                i += 1
                j -= 1
            next_queue = []
            for node in queue:
                if node:
                    next_queue += [node.left, node.right]
            queue = next_queue
        return True

    def is_symmetric_recursive(self, root: TreeNode) -> bool:
        if not root:
            return True

        def check(l_node: TreeNode, r_node: TreeNode):
            if not l_node and not r_node:
                return True
            if not (l_node and r_node):
                return False
            if l_node.val != r_node.val:
                return False
            return check(l_node.left, r_node.right) and \
                   check(l_node.right, r_node.left)

        return check(root.left, root.right)
