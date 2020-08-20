"""133. Clone Graph
https://leetcode.com/problems/clone-graph/
"""


class Solution:
    def clone_graph(self, node: 'Node') -> 'Node':
        def dfs(v: Node):
            if v in mark:
                return mark[v]
            clone = Node(v.val)
            mark[v] = clone
            clone_neighbors = []
            for e in v.neighbors:
                clone_neighbors.append(dfs(e))
            clone.neighbors = clone_neighbors
            return mark[v]

        if not node:
            return None
        mark = {}
        return dfs(node)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if not neighbors else []
