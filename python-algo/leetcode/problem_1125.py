"""1125. Smallest Sufficient Team
https://leetcode.com/problems/smallest-sufficient-team/
"""
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m, n = len(people), len(req_skills)
        skill_index = dict()
        for i, skill in enumerate(req_skills):
            skill_index[i] = skill
        dp = [[] for _ in range(1 << n)]
        for i in range(m):
            cur_skill = 0
            for s in people[i]:
                cur_skill |= 1 << skill_index[s]
            for j in range(len(dp)):
                if not dp[j]:
                    continue
                cmb = j | cur_skill
                if not dp[cmb] or len(dp[j]) + 1 < len(dp[cmb]):
                    dp[cmb] = dp[j][:]
                    dp[cmb].append(i)
        return dp[-1]
