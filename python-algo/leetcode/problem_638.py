"""638. Shopping Offers
https://leetcode.com/problems/shopping-offers/
"""
from functools import lru_cache
from typing import List


class Solution:
    def shopping_offers(self, price: List[int], special: List[List[int]],
                        needs: List[int]) -> int:
        n = len(price)
        valid_special = []
        for i in range(len(special)):
            total = 0
            for j in range(n):
                total += price[j] * special[i][j]
            if total > special[i][-1]:
                valid_special.append(special[i])

        @lru_cache(None)
        def dfs(cur_needs) -> int:
            cur_needs = list(cur_needs)
            ret = sum(need * price[_] for _, need in enumerate(cur_needs))
            for sp in valid_special:
                next_needs = []
                for i in range(n):
                    if sp[i] > cur_needs[i]:
                        break
                    next_needs.append(cur_needs[i] - sp[i])
                if len(next_needs) == len(price):
                    ret = min(ret, dfs(tuple(next_needs)) + sp[-1])
            return ret

        return dfs(tuple(needs))


if __name__ == '__main__':
    sol = Solution()
    print(sol.shopping_offers([2,3,4],[[1,1,0,4],[2,2,1,9]],[1,2,1]))
