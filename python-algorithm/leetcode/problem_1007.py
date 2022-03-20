"""1007. Minimum Domino Rotations For Equal Row
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
"""
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotate(l1: List[int], x: int, is_top: bool) -> int:
            nums = bottoms if is_top else tops
            for pos in l1:
                if nums[pos] != x:
                    return -1
            return len(l1)

        n = len(tops)
        store1 = [[] for _ in range(7)]
        store2 = [[] for _ in range(7)]
        for i in range(n):
            store1[tops[i]].append(i)
            store2[bottoms[i]].append(i)
        ans = n + 1
        for i in range(1, 7):
            tmp = 0
            ok = True
            for j in range(1, 7):
                if j != i:
                    ret = rotate(store1[j], i, True)
                    if ret == -1:
                        ok = False
                        break
                    tmp += ret
            if ok:
                ans = min(ans, tmp)
        for i in range(1, 7):
            tmp = 0
            ok = True
            for j in range(1, 7):
                if j != i:
                    ret = rotate(store2[j], i, False)
                    if ret == -1:
                        ok = False
                        break
                    tmp += ret
            if ok:
                ans = min(ans, tmp)
        return ans if ans <= n else -1
