"""587. Erect the Fence
https://leetcode.com/problems/erect-the-fence/
"""
from typing import List


class Solution:
    def outer_trees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def is_between(p: List[int], i: List[int], q: List[int]) -> bool:
            a = p[0] <= i[0] <= q[0] or p[0] >= i[0] >= q[0]
            b = p[1] <= i[1] <= q[1] or p[1] >= i[1] >= q[1]
            return a and b

        n = len(trees)
        hull = set()
        if n < 4:
            return trees
        left = 0
        for i in range(n):
            if trees[i][0] < trees[left][0]:
                left = i
        p = left
        while True:
            q = (p + 1) % n
            for i in range(n):
                if orientation(trees[p], trees[i], trees[q]) < 0:
                    q = i
            for i in range(n):
                if i != p and i != q and orientation(trees[p], trees[i], trees[q]) == 0 and is_between(trees[p], trees[i], trees[q]):
                    hull.add(tuple(trees[i]))
            hull.add(tuple(trees[q]))
            p = q
            if p == left:
                break
        ans = []
        for h in hull:
            ans.append(list(h))
        return ans
