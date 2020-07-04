"""979. Distribute Coins in Binary Tree
https://leetcode.com/problems/distribute-coins-in-binary-tree/

Given the root of a binary tree with N nodes, each node in the tree has 
node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node 
to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Note:
  1<= N <= 100
  0 <= node.val <= N
"""
from common.tree_node import TreeNode


class Solution:
    def distribute_coins(self, root: 'TreeNode') -> 'int':
        count = 0

        def recursive_count(node: 'TreeNode') -> 'int':
            nonlocal count
            if node is None:
                return 0
            if node.left is None and node.right is None:
                count += abs(node.val - 1)
                return node.val - 1
            node.val += recursive_count(node.left)
            node.val += recursive_count(node.right)
            count += abs(node.val - 1)
            return node.val - 1

        recursive_count(root)
        return count
