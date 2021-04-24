"""897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/

Given the root of a binary search tree, rearrange the tree in in-order so
that the leftmost node in the tree is now the root of the tree, and every
node has no left child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:

Input: root = [5,1,7]
Output: [1,null,5,null,7]

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def increasing_bst(self, root: TreeNode) -> TreeNode:
        def recursive_traversal(node: TreeNode) -> List[int]:
            if not node:
                return []
            ret = []
            ret += recursive_traversal(node.left)
            ret.append(node.val)
            ret += recursive_traversal(node.right)
            return ret

        if not root:
            return root
        seq = recursive_traversal(root)
        dummy = cur = TreeNode(-1)
        for val in seq:
            cur.right = TreeNode(val)
            cur = cur.right
        return dummy.right

    def increasing_bst2(self, root: TreeNode) -> TreeNode:
        dummy = cur = TreeNode(-1)
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                cur.right = TreeNode(root.val)
                cur = cur.right
                root = root.right
        return dummy.right

    def increasing_bst3(self, root: TreeNode) -> TreeNode:
        dummy = cur = TreeNode(-1)
        stack = list()
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root.left = None
                cur.right = root
                cur = cur.right
                root = root.right
        return dummy.right


if __name__ == '__main__':
    sol = Solution()
    node = TreeNode(5)
    l_node = TreeNode(1)
    r_node = TreeNode(7)
    node.left = l_node
    node.right = r_node
    ans = sol.increasing_bst3(node)
    print(ans)
