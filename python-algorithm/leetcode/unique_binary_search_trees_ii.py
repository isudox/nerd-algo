"""95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, generate all structurally unique BST's (binary search
trees) that store values 1 ... n.

Example:


Input: 3
Output:
[
[1,null,3,2],
[3,2,null,1],
[3,1,null,null,2],
[2,1,3],
[1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

⁠  1         3     3      2      1
⁠   \       /     /      / \      \
⁠    3     2     1      1   3      2
⁠   /     /       \                 \
⁠  2     1         2                 3
"""
from typing import List

from common.tree_node import TreeNode


class Solution:
    def generate_trees(self, n: int) -> List[TreeNode]:
        assert n > 0
        if n == 1:
            return [TreeNode(1)]
        ans = []

        return ans

