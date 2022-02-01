package com.leetcode;

/**
 * 121. Best Time to Buy and Sell Stock
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 */
public class Problem121 {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int min = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > min) {
                if (ans < prices[i] - min) {
                    ans = prices[i] - min;
                }
            } else if (prices[i] < min) {
                min = prices[i];
            }
        }
        return ans;
    }
}
