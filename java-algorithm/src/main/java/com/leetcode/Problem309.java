package com.leetcode;

/**
 * 309. Best Time to Buy and Sell Stock with Cooldown
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
 */
public class Problem309 {
    int[] prices;

    public int maxProfit(int[] prices) {
        this.prices = prices;
        int[][][] memo = new int[prices.length][2][2];
        return dfs(0, 0, 0, memo);
    }

    private int dfs(int i, int hasStock, int soldLastDay, int[][][] memo) {
        if (i == prices.length) {
            return 0;
        }
        if (memo[i][hasStock][soldLastDay] != 0) {
            return memo[i][hasStock][soldLastDay];
        }
        int profit = 0;
        if (hasStock == 1) {
            // 1. sell
            profit = Math.max(profit, prices[i] + dfs(i + 1, 0, 1, memo));
            // 2. skip
            profit = Math.max(profit, dfs(i + 1, 1, 0, memo));
        } else if (soldLastDay == 1) {
            // skip
            profit = Math.max(profit, dfs(i + 1, 0, 0, memo));
        } else {
            // 1. buy
            profit = Math.max(profit, -prices[i] + dfs(i + 1, 1, 0, memo));
            // 2. skip
            profit = Math.max(profit, dfs(i + 1, 0, 0, memo));
        }
        return memo[i][hasStock][soldLastDay] = profit;
    }
}
