package com.leetcode;

import java.util.List;

/**
 * 2218. Maximum Value of K Coins From Piles
 * https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
 */
public class Problem2218 {
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        int n = piles.size();
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                int sum = 0;
                for (int x = 0; x <= Math.min(piles.get(i - 1).size(), j); x++) {
                    if (x > 0) {
                        sum += piles.get(i - 1).get(x - 1);
                    }
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - x] + sum);
                }
            }
        }
        return dp[n][k];
    }
}
