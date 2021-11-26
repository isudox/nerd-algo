from common.tree_node import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root and root.val != val:
            root = root.left if root.val > val else root.right
        return root
