"""319. Bulb Switcher
https://leetcode.com/problems/bulb-switcher/
"""


class Solution:
    def bulb_switch(self, n: int) -> int:
        i = 1
        while i * i <= n:
            i += 1
        return i - 1
