"""1482. Minimum Number of Days to Make m Bouquets
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent
flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the
bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m
bouquets from the garden. If it is impossible to make m bouquets return
-1.

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower
bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6
flowers. We only have 5 flowers so it is impossible to get the needed
bouquets and we return -1.

Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot
make another bouquet from the last three flowers that bloomed because they
are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Example 4:

Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
Output: 1000000000
Explanation: You need to wait 1000000000 days to have a flower ready for a
bouquet.

Example 5:

Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
Output: 9

Constraints:

bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
"""
from typing import List


class Solution:
    def min_days(self, bloom_day: List[int], m: int, k: int) -> int:
        def helper(limit: int) -> bool:
            flowers, adj = 0, 0
            for i in range(len(bloom_day)):
                # 优化: 当剩余花盆数量不足以制作所需花束，提前结束
                if bloom_day[i] > limit:
                    adj = 0
                else:
                    adj += 1
                    if adj == k:
                        flowers += 1
                        # 优化: 当已经制作完成所需花束，提前结束
                        if flowers == m:
                            return True
                        adj = 0
                if adj == 0 and len(bloom_day) - i - 1 < (m - flowers) * k:
                    return False
            return False

        if len(bloom_day) < m * k:
            return -1
        hi = lo = bloom_day[0]
        for day in bloom_day:
            if day > hi:
                hi = day
            if day < lo:
                lo = day
        while lo < hi:
            mid = (lo + hi) >> 1
            if helper(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
