"""993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

In a binary tree, the root node is at depth 0, and children of each depth k
node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have
different parents.

We are given the root of a binary tree with unique values, and the values x
and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are
cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
from common.tree_node import TreeNode


class Solution:
    def is_cousins(self, root: TreeNode, x: int, y: int) -> bool:
        store = {x: -1, y: -1}
        queue = [root]
        depth = 0
        found = False
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                        (node.left.val == y and node.right.val == x):
                        return False
                if node.val == x or node.val == y:
                    store[node.val] = depth
                    found = True
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if found:
                return store[x] == store[y]
            depth += 1
        return store[x] == store[y]
