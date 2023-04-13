"""559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        ans = 1
        for node in root.children:
            ans = max(ans, self.maxDepth(node) + 1)
        return ans
