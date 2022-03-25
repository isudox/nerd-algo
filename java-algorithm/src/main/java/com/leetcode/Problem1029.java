package com.leetcode;

import java.util.Arrays;

/**
 * 1029. Two City Scheduling
 * https://leetcode.com/problems/two-city-scheduling/
 */
public class Problem1029 {
    public int twoCitySchedCost(int[][] costs) {
        Arrays.sort(costs, (o1, o2) -> (o1[0] - o1[1]) - (o2[0] - o2[1]));
        int ans = 0;
        int n = costs.length / 2;
        for (int i = 0; i < n; i++) {
            ans += costs[i][0] + costs[i + n][1];
        }
        return ans;
    }
}
