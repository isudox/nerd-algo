"""863. All Nodes Distance K in Binary Tree
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
from typing import List
from common.tree_node import TreeNode
import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root: TreeNode):
            if root.left:
                graph[root.val].add(root.left.val)
                graph[root.left.val].add(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].add(root.right.val)
                graph[root.right.val].add(root.val)
                dfs(root.right)

        graph = collections.defaultdict(set)
        dfs(root)
        queue = [target.val]
        visited = {target.val}
        for i in range(k):
            next_queue = []
            while queue:
                cur = queue.pop()
                for node in graph[cur]:
                    if node not in visited:
                        visited.add(node)
                        next_queue.append(node)
            queue = next_queue
        return queue
