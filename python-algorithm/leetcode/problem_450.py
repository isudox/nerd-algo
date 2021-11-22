"""450.
"""


from typing import Optional
from common.tree_node import TreeNode


class Solution:
    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node: TreeNode) -> int:
            while node.left:
                node = node.left
            return node.val

        def remove(node: TreeNode) -> Optional[TreeNode]:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            node.val = find_min(node.right)
            node.right = self.delete_node(node.right, node.val)
            return node

        if not root:
            return None
        if root.val > key:
            root.left = self.delete_node(root.left, key)
        elif root.val < key:
            root.right = self.delete_node(root.right, key)
        else:
            return remove(root)
        return root