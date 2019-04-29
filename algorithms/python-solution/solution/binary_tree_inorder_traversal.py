"""94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/


Given a binary tree, return the in-order traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def iterative_inorder_traversal(self, root: TreeNode) -> List[int]:
        """
        iterative traversal
        :param root:
        :return:
        """
        if not root:
            return []
        ans = []
        stack = []
        cur_node = root
        while cur_node.left:
            stack.append(cur_node)
            cur_node = cur_node.left
        ans.append(cur_node.val)

        return ans

    def recursive_inorder_traversal(self, root: TreeNode) -> List[int]:
        """
        recursively traversal, process left if needed, then val, at last right
        :param root:
        :return:
        """
        if not root:
            return []
        ans = []
        ans += self.recursive_inorder_traversal(root.left)
        ans.append(root.val)
        ans += self.recursive_inorder_traversal(root.right)
        return ans


if __name__ == "__main__":
    solution = Solution()
    root_node = TreeNode(1)
    root_node.right = TreeNode(2)
    root_node.right.left = TreeNode(3)

    print(solution.recursive_inorder_traversal(None))
    print(solution.iterative_inorder_traversal(None))
    print(solution.recursive_inorder_traversal(root_node))
    print(solution.iterative_inorder_traversal(root_node))
