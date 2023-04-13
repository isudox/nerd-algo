"""1203. Sort Items by Groups Respecting Dependencies
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
"""
import collections
from typing import List


class Solution:
    def sort_items(self, n: int, m: int, group: List[int], before_items: List[List[int]]) -> List[int]:
        def get_top_order(graph, indegree):
            top_order = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                v = stack.pop()
                top_order.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        stack.append(u)
            return top_order if len(top_order) == len(graph) else []

        # STEP 1: Create a new group for each item that belongs to no group.
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        # STEP 2: Build directed graphs for items and groups.
        graph_items = [[] for _ in range(n)]
        indegree_items = [0] * n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0] * m
        for u in range(n):
            for v in before_items[u]:
                graph_items[v].append(u)
                indegree_items[u] += 1
                if group[u] != group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1

        # STEP 3: Find topological orders of items and groups.
        item_order = get_top_order(graph_items, indegree_items)
        group_order = get_top_order(graph_groups, indegree_groups)
        if not item_order or not group_order:
            return []

        # STEP 4: Find order of items within each group.
        order_within_group = collections.defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        # STEP 5. Combine ordered groups.
        res = []
        for group in group_order:
            res += order_within_group[group]
        return res
