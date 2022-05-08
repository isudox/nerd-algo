import functools
from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        @functools.lru_cache(None)
        def helper(node: TreeNode):
            cur = node.val
            cnt = 1
            left = [0, 0]
            right = [0, 0]
            if node.left:
                left = helper(node.left)
            if node.right:
                right = helper(node.right)
            cur += left[0] + right[0]
            cnt += left[1] + right[1]
            if cur // cnt == node.val:
                nonlocal ans
                ans += 1
            return [cur, cnt]

        ans = 0
        helper(root)
        return ans


if __name__ == '__main__':
    root = TreeNode(4)
    n8 = TreeNode(8)
    n5 = TreeNode(5)
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    root.left = n8
    root.right = n5
    n8.left = n0
    n8.right = n1
    n5.right = n6
    sol = Solution()
    print(sol.averageOfSubtree(root))
    print(sol.averageOfSubtree(TreeNode(1)))
