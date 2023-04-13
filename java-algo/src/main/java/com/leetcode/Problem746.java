package com.leetcode;

/**
 * 746. Min Cost Climbing Stairs
 * https://leetcode.com/problems/min-cost-climbing-stairs/
 */
public class Problem746 {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if (n == 2) return Math.min(cost[0], cost[1]);
        int[] dp = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[n];
    }
}
