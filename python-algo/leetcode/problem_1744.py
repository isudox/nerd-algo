"""1744. Can You Eat Your Favorite Candy on Your Favorite Day?
https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

You are given a (0-indexed) array of positive integers candiesCount where
candiesCount[i] represents the number of candies of the i^th type you have.
You are also given a 2D array queries where queries[i] = [favoriteTypei,
favoriteDayi, dailyCapi].

You play a game with the following rules:

You start eating candies on day 0.
You cannot eat any candy of type i unless you have eaten all candies of type
i - 1.
You must eat at least one candy per day until you have eaten all the
candies.

Construct a boolean array answer such that answer.length == queries.length
and answer[i] is true if you can eat a candy of type favoriteTypei on day
favoriteDayi without eating more than dailyCapi candies on any day, and false
otherwise. Note that you can eat different types of candy on the same day,
provided that you follow rule 2.

Return the constructed array answer.

Example 1:

Input: candiesCount = [7,4,5,3,8], queries =
[[0,2,2],[4,2,4],[2,13,1000000000]]
Output: [true,false,true]
Explanation:
1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1,
you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
  If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0
and 4 candies (type 0 and type 1) on day 1.
  On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot
eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.

Example 2:

Input: candiesCount = [5,2,6,4,1], queries =
[[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
Output: [false,true,true,false,false]

Constraints:
1 <= candiesCount.length <= 10^5
1 <= candiesCount[i] <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 3
0 <= favoriteTypei < candiesCount.length
0 <= favoriteDayi <= 10^9
1 <= dailyCapi <= 10^9
"""
import bisect
from typing import List


class Solution:
    def can_eat(self, candies_count: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        pre_sum = [0] * len(candies_count)
        for i, cnt in enumerate(candies_count):
            pre_sum[i] = cnt + (pre_sum[i - 1] if i > 0 else 0)
        for i, (k, day, cap) in enumerate(queries):
            lo, hi = day + 1, cap * (day + 1)
            idx1 = bisect.bisect_left(pre_sum, lo)
            idx2 = bisect.bisect_left(pre_sum, hi)
            ans[i] = idx1 <= k <= idx2
        return ans

    def can_eat2(self, candies_count: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        pre_sum = [0] * len(candies_count)
        for i, cnt in enumerate(candies_count):
            pre_sum[i] = cnt + (pre_sum[i - 1] if i > 0 else 0)
        for i, (k, day, cap) in enumerate(queries):
            lo, hi = day + 1, cap * (day + 1)
            left = 1 + (0 if k == 0 else pre_sum[k - 1])
            right = pre_sum[k]
            if lo <= right and hi >= left:
                ans[i] = True
        return ans
