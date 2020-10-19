"""145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given a binary tree, return the post-order traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def iterative_postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans, stack = [], []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                node = stack[-1]
                if node.right:
                    cur = node.right
                else:
                    ans.append(node.val)
                    stack.pop()
        return ans

    def recursive_postorder_traversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        ans += self.recursive_postorder_traversal(root.left)
        ans += self.recursive_postorder_traversal(root.right)
        ans.append(root.val)
        return ans


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    sub1 = TreeNode(2)
    sub2 = TreeNode(3)
    root.right = sub1
    sub1.left = sub2
    print(sol.recursive_postorder_traversal(root))
    print(sol.iterative_postorder_traversal(root))
