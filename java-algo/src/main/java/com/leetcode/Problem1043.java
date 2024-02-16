package com.leetcode;

/**
 * 1043. Partition Array for Maximum Sum
 * https://leetcode.com/problems/partition-array-for-maximum-sum/
 */
public class Problem1043 {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int max = arr[i - 1];
            for (int j = i - 1; j >= 0 && j >= i - k; j--) {
                dp[i] = Math.max(dp[i], dp[j] + max * (i - j));
                if (j > 0) {
                    max = Math.max(max, arr[j - 1]);
                }
            }
        }
        return dp[n];
    }
}
