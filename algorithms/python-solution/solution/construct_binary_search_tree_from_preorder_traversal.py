"""1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal


Return the root node of a binary search tree that matches the given preorder
traversal.

(Recall that a binary search tree is a binary tree where for every node, any
descendant of node.left has a value < node.val, and any descendant of
node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left, then
traverses node.right.)



Example 1:


Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
![](https://assets.leetcode.com/uploads/2019/03/06/1266.png)



Note: 


1 <= preorder.length <= 100
The values of preorder are distinct.
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def bst_from_preorder(self, preorder: List[int]) -> TreeNode:

        def backtrack(start: int, end: int) -> TreeNode:
            """
            Recursively generate TreeNode by sub list of preorder.
            :param start: the start index of sub list.
            :param end: the end index of sub list.
            :return: the generated TreeNode.
            """
            val = preorder[start]
            root = TreeNode(val)
            if start == end:
                return root
            i = start + 1
            split = -1
            has_split = False
            # find the split num of the sub list if it exists.
            while i <= end:
                if preorder[i] > val:
                    has_split = True
                    split = i
                    break
                i += 1
            if has_split:
                if start + 1 <= split - 1:
                    # process the left children TreeNode
                    root.left = backtrack(start + 1, split - 1)
                if split <= end:
                    # process the right children TreeNode
                    root.right = backtrack(split, end)
            else:
                if start + 1 <= end:
                    # process the left children TreeNode
                    root.left = backtrack(start + 1, end)
            return root

        return backtrack(0, len(preorder) - 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.bst_from_preorder([8, 5, 1, 7, 10, 12]))
    print(solution.bst_from_preorder([4, 2]))
