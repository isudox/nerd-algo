"""993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/
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
