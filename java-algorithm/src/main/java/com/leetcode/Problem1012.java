package com.leetcode;

import java.util.Arrays;

public class Problem1012 {
    int[][] dp;

    public int numDupDigitsAtMostN(int n) {
        String sn = String.valueOf(n);
        dp = new int[sn.length()][1 << 10];
        for (int i = 0; i < sn.length(); i++) {
            Arrays.fill(dp[i], -1);
        }
        return n + 1 - helper(0, sn, 0, true);
    }

    private int helper(int mask, String sn, int i, boolean same) {
        if (i == sn.length()) {
            return 1;
        }
        if (!same && dp[i][mask] >= 0) {
            return dp[i][mask];
        }
        int ret = 0, t = same ? (sn.charAt(i) - '0') : 9;
        for (int j = 0; j <= t; j++) {
            if ((mask & (1 << j)) != 0) {
                continue;
            }
            ret += helper(mask == 0 && j == 0 ? mask : mask | (1 << j), sn, i + 1, same && j == t);
        }
        if (!same) {
            dp[i][mask] = ret;
        }
        return ret;
    }
}
