package com.leetcode;

import java.util.Arrays;

/**
 * 354. Russian Doll Envelopes
 * https://leetcode.com/problems/russian-doll-envelopes/
 */
public class Problem354 {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes.length == 0) {
            return 0;
        }
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        int[] dp = new int[envelopes.length];
        int ans = 0;
        for (int[] e : envelopes) {
            int idx = Arrays.binarySearch(dp, 0, ans, e[1]);
            if (idx < 0) {
                idx = -(idx + 1);
            }
            dp[idx] = e[1];
            if (idx == ans) {
                ans++;
            }
        }
        return ans;
    }
}
