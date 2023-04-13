"""1208. Get Equal Substrings Within Budget
https://leetcode.com/problems/get-equal-substrings-within-budget/

Constraints:

    1 <= s.length, t.length <= 10^5
    0 <= maxCost <= 10^6
    s and t only contain lower case English letters.
"""


class Solution:
    def equal_substring(self, s: str, t: str, max_cost: int) -> int:
        def get_cost(idx: int) -> int:
            return abs(ord(s[idx]) - ord(t[idx]))

        i, j = 0, 0
        used, ans = 0, 0
        n = min(len(s), len(t))
        while j < n:
            cost = get_cost(j)
            if used + cost <= max_cost:
                used += cost
                j += 1
                ans = max(ans, j - i)
            else:
                used -= get_cost(i)
                i += 1
        return ans

    def equal_substring_2(self, s: str, t: str, max_cost: int) -> int:
        n = min(len(s), len(t))
        costs = []
        for i in range(n):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        ans = 0
        i = j = 0
        cost = 0
        while j < n:
            cost += costs[j]
            if cost > max_cost:
                ans = max(ans, j - i)
                cost = cost - costs[j] - costs[i]
                i += 1
            else:
                j += 1
                ans = max(ans, j - i)
        return max(ans, j - i)

    def equal_substring_3(self, s: str, t: str, max_cost: int) -> int:
        n = min(len(s), len(t))
        i = j = 0
        cost = 0
        ans = 0
        while j < n:
            temp = abs(ord(s[j]) - ord(t[j]))
            if cost + temp > max_cost:
                ans = max(ans, j - i)
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            else:
                cost += temp
                j += 1
        return max(ans, j - i)
