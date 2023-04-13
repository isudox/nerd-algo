"""971. Flip Binary Tree To Match Preorder Traversal
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
Given a binary tree with N nodes, each node has a different value from
{1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the
right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from
the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current
node's value, then preorder-traverse the left child, then preorder-traverse the
right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of
the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may
return the answer in any order.

If we cannot do so, then return the list [-1].

Example 1:
  Input: root = [1,2], voyage = [2,1]
  Output: [-1]

Example 2:
  Input: root = [1,2,3], voyage = [1,3,2]
  Output: [1]

Example 3:
  Input: root = [1,2,3], voyage = [1,2,3]
  Output: []

Note:
  1 <= N <= 100
"""
from common.tree_node import TreeNode


class Solution:
    def flip_match_voyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        stack, ans = [root], []
        i, size = 0, len(voyage)

        while len(stack) and i < size:
            temp = stack.pop()
            if temp.val != voyage[i]:
                break
            i += 1
            if i < size:
                if temp.left and temp.left.val != voyage[i]:
                    ans.append(temp.val)
                    stack.append(temp.left)
                    if temp.right:
                        stack.append(temp.right)
                else:
                    if temp.right:
                        stack.append(temp.right)
                    if temp.left:
                        stack.append(temp.left)
        if i != size:
            return [-1]
        return ans
