"""199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/

Given the root of a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top to
bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import List
from common.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            ans.append(queue[-1].val)
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
