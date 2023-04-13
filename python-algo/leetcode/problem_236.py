"""236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
of itself according to the LCA definition.

Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(start: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
            if start == target:
                path.append(target)
                return True
            path.append(start)
            if start.left:
                if not find_path(start.left, target, path):
                    path.pop(-1)
                else:
                    return True
            if start.right:
                if not find_path(start.right, target, path):
                    path.pop(-1)
                else:
                    return True
            return False
        path_to_p, path_to_q = [], []
        find_path(root, p, path_to_p)
        find_path(root, q, path_to_q)
        for i in range(len(path_to_p) - 1, -1, -1):
            if path_to_p[i] in path_to_q:
                return path_to_p[i]
