"""1705. Maximum Number of Eaten Apples
https://leetcode.com/problems/maximum-number-of-eaten-apples/
"""
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        if not apples:
            return 0
        ans = 0
        all_day = 0
        for i in range(len(apples)):
            all_day = max(all_day, i + days[i])
        store = [0] * (all_day + 1)
        mark_day = 0
        for today in range(all_day):
            if today < len(apples):
                store[today + days[today]] += apples[today]
            for i in range(max(mark_day, today), all_day):
                if store[i + 1] > 0:
                    store[i + 1] -= 1
                    ans += 1
                    mark_day = i
                    break
        return ans


if __name__ == '__main__':
    sol = Solution()
    # print(sol.eatenApples([1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
    print(sol.eatenApples([2, 1, 1, 4, 5], [10, 10, 6, 4, 2]))
    # print(sol.eatenApples([1,10,17,10,12,6,20,8,8,22,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,5,2,1,0,0,0,0,0,0,23],[19999,11,18,22,5,2,14,5,20,7,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,1,4,2,7,0,0,0,0,0,0,1]))
