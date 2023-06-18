package com.leetcode;

import java.util.Arrays;

/**
 * 1494. Parallel Courses II
 * https://leetcode.com/problems/parallel-courses-ii/
 */
public class Problem1494 {
    public int minNumberOfSemesters(int n, int[][] relations, int k) {
        int[] dp = new int[1 << n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        int[] need = new int[1 << n];
        for (int[] relation : relations) {
            need[1 << (relation[1] - 1)] |= 1 << (relation[0] - 1);
        }
        dp[0] = 0;
        for (int i = 1; i < (1 << n); i++) {
            need[i] = need[i & (i - 1)] | need[i & -i];
            if ((need[i] | i) != i) {
                continue;
            }
            int valid = i ^ need[i];
            if (Integer.bitCount(valid) <= k) {
                dp[i] = Math.min(dp[i], dp[i ^ valid] + 1);
            } else {
                for (int j = valid; j > 0; j = (j - 1) & valid) {
                    if (Integer.bitCount(j) <= k) {
                        dp[i] = Math.min(dp[i], dp[i ^ j] + 1);
                    }
                }
            }
        }
        return dp[dp.length - 1];
    }
}
