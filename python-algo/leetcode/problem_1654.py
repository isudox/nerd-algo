"""1654. Minimum Jumps to Reach Home
https://leetcode.com/problems/minimum-jumps-to-reach-home/
TODO
"""
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        forbidden = set(forbidden)
        lo, hi = 0, max(max(forbidden) + a, x) + b
        visited = set()
        visited.add(0)
        ans = 0
        q = [(0, 0)]
        while q:
            ans += 1
            n = len(q)
            for i in range(n):
                pos, d = q.pop(0)
                if pos + a == x:
                    return ans
                if lo <= (pos + a) <= hi and (pos + a) not in forbidden:
                    visited.add(pos + a)
                    q.append((pos + a, 1))
                if pos >= b and d >= 0:  # can backward
                    if pos - b == x:
                        return ans
                    if lo <= (pos - b) <= hi and (pos - b) not in forbidden:
                        visited.add(pos - b)
                        q.append((pos - b, -1))
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29,98,80))
