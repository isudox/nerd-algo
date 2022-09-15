"""672. Bulb Switcher II
https://leetcode.com/problems/bulb-switcher-ii/
"""


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return (presses > 0) + 1
        if n == 2:
            return (presses > 1) + (presses > 0) * 2 + 1
        if presses == 0:
            return 1
        if presses == 1:
            return 4
        if presses == 2:
            return 7
        return 8
