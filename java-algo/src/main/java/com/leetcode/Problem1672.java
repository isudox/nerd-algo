package com.leetcode;

/**
 * 1672. Richest Customer Wealth
 * https://leetcode.com/problems/richest-customer-wealth/
 */
public class Problem1672 {
    public int maximumWealth(int[][] accounts) {
        int ans = 0;
        for (int[] account : accounts) {
            int sum = 0;
            for (int money : account) {
                sum += money;
            }
            if (sum > ans) {
                ans = sum;
            }
        }
        return ans;
    }
}
