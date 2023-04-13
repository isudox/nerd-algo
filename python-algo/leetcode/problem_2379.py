"""2379. Minimum Recolors to Get K Consecutive Black Blocks
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                cnt += 1
        ans = cnt
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'B' and blocks[i] == 'W':
                cnt += 1
            elif blocks[i - k] == 'W' and blocks[i] == 'B':
                cnt -= 1
            if cnt < ans:
                ans = cnt
        return ans
