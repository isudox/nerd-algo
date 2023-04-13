package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 1125. Smallest Sufficient Team
 * https://leetcode.cn/problems/smallest-sufficient-team/
 */
public class Problem1125 {
    public int[] smallestSufficientTeam(String[] req_skills, List<List<String>> people) {
        int n = req_skills.length, m = people.size();
        Map<String, Integer> skillIndex = new HashMap<>();
        for (int i = 0; i < n; i++) {
            skillIndex.put(req_skills[i], i);
        }
        List<Integer>[] dp = new List[1 << n];
        dp[0] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int curSkill = 0;
            for (String s : people.get(i)) {
                curSkill |= 1 << skillIndex.get(s);
            }
            for (int prev = 0; prev < dp.length; prev++) {
                if (dp[prev] == null) {
                    continue;
                }
                int comb = prev | curSkill;
                if (dp[comb] == null || dp[prev].size() + 1 < dp[comb].size()) {
                    dp[comb] = new ArrayList<>(dp[prev]);
                    dp[comb].add(i);
                }
            }
        }
        return dp[(1 << n) - 1].stream().mapToInt(i -> i).toArray();
    }
}
