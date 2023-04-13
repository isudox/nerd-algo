"""1202. Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/

You are given a string s, and an array of pairs of indices in the string pairs
where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explanation:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explanation:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explanation:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:

    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s only contains lower case English letters.
"""
import collections
from typing import List


class Solution:
    def smallest_string_with_swaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))

            def union(self, x, y):
                self.parent[self.find(x)] = self.find(y)

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        n = len(s)
        if n == 0:
            return s
        uf, res, graph = UnionFind(n), [], collections.defaultdict(list)
        for a, b in pairs:
            uf.union(a, b)
        for i in range(n):
            graph[uf.find(i)].append(s[i])
        for comp_id in graph.keys():
            graph[comp_id].sort(reverse=True)
        for i in range(n):
            res.append(graph[uf.find(i)].pop())
        return ''.join(res)
