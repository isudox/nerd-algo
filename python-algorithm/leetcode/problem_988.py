"""988. Smallest String Starting From Leaf
https://leetcode.com/problems/smallest-string-starting-from-leaf/

Given the root of a binary tree, each node has a value from 0 to 25
representing the letters 'a' to 'z': a value of 0 represents 'a',
a value of 1 represents 'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller:
for example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.)
"""
from common.tree_node import TreeNode


class Solution:
    def smallest_from_leaf(self, root: 'TreeNode') -> 'str':
        return ''
