package com.leetcode;

/**
 * 188. Best Time to Buy and Sell Stock IV
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
 */
public class Problem188 {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        k = Math.min(k, n / 2);
        if (n < 2 || k == 0) return 0;
        int[][] buy = new int[n][k + 1];  // buy[i][j] 表示截止到第 i 天，累计交易 j 次，且持有股票的最大盈利
        int[][] sell = new int[n][k + 1]; // sell[i][j] 表示截止到第 i 天，累计交易 j 次，且无股票的最大盈利
        buy[0][0] = -prices[0];
        sell[0][0] = 0;
        for (int i = 1; i < n; i++) {
            buy[0][i] = sell[0][i] = -1000 * 1000;
        }
        for (int i = 1; i <= k; i++) {
            buy[i][0] = Math.max(buy[i - 1][0], sell[i - 1][0] - prices[i]);
            for (int j = 1; j <= k; j++) {
                buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
                sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
            }
        }
        int ans = 0;
        for (int x : sell[n - 1]) {
            if (x > ans) ans = x;
        }
        return ans;
    }
}
