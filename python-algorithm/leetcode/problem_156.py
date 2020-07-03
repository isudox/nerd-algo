"""156. Binary Tree Upside Down
https://leetcode-cn.com/problems/binary-tree-upside-down

Given a binary tree where all the right nodes are either leaf nodes with
a sibling (a left node that shares the same parent node) or empty,
flip it upside down and turn it into a tree where the original right nodes
turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-upside-down
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from common.tree_node import TreeNode


class Solution:
    def upside_down_binary_tree(self, root: TreeNode) -> TreeNode:
        new_root = None
        parent_right_child = None
        # left child -> root, root -> right child, right child -> left child
        while root:
            left_child = root.left
            root.left = parent_right_child
            parent_right_child = root.right
            root.right = new_root
            new_root = root
            root = left_child

        return new_root
