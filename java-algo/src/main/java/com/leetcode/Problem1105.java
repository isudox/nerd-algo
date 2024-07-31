package com.leetcode;

import java.util.Arrays;

/**
 * 1105. Filling Bookcase Shelves
 * https://leetcode.com/problems/filling-bookcase-shelves/
 */
public class Problem1105 {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int n = books.length;
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 1000001);
        dp[0] = 0;  // dp[i] = the answer of books[0:i]
        for (int i = 0; i < n; i++) {
            int width = 0, height = 0;
            for (int j = i; j >= 0; j--) {
                width += books[j][0];
                if (width > shelfWidth) {
                    break;
                }
                height = Math.max(height, books[j][1]);
                dp[i + 1] = Math.min(dp[i + 1], dp[j] + height);
            }
        }
        return dp[n];
    }
}
