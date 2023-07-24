"""771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/description/
"""


class Solution:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        ans = 0
        js = set(jewels)
        for s in stones:
            if s in js:
                ans += 1
        return ans
