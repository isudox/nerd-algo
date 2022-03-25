"""661. Image Smoother
https://leetcode.com/problems/image-smoother/
"""
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cur, cnt = 0, 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            cur += img[x][y]
                            cnt += 1
                ans[i][j] = int(cur / cnt)
        return ans
