"""399. Evaluate Division
https://leetcode.com/problems/evaluate-division/

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Constraints:

    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from typing import List
from typing import Set
from collections import defaultdict


class Solution:
    def calc_equation(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:
        def dfs(start: str, end: str, visited: Set[str]) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            key = start + '_' + end
            if key in edges:
                return edges[key]
            if start in visited:
                return 0
            visited.add(start)
            value = 0
            for point in graph[start]:
                value = dfs(point, end, visited) * edges[start + '_' + point]
                if value != 0:
                    edges[key] = value
                    break
            visited.remove(start)
            return value

        graph = defaultdict(set)
        edges = defaultdict()
        n = len(values)
        for i in range(n):
            graph[equations[i][0]].add(equations[i][1])
            graph[equations[i][1]].add(equations[i][0])
            edges[equations[i][0] + '_' + equations[i][1]] = values[i]
            edges[equations[i][1] + '_' + equations[i][0]] = float(1 / values[i])
        ans = []
        for query in queries:
            cur = dfs(query[0], query[1], set())
            if cur == 0:
                ans.append(-1.0)
            else:
                ans.append(cur)
        return ans
