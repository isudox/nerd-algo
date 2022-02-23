"""133. Clone Graph
https://leetcode.com/problems/clone-graph/
"""


class Solution:
    def clone_graph(self, node: 'Node') -> 'Node':
        def dfs(v: Node):
            if v.val in visited:
                return visited[v.val]
            ret = Node(v.val)
            visited[v.val] = ret
            for e in v.neighbors:
                ret.neighbors.append(dfs(e))
            return ret

        if not node:
            return node
        visited = {}
        return dfs(node)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if not neighbors else []
