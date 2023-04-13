package com.leetcode;

import java.util.Arrays;

/**
 * 2028. Find Missing Observations
 * https://leetcode.com/problems/find-missing-observations/
 */
public class Problem2028 {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int total = mean * (n + rolls.length);
        int sum1 = 0;
        for (int roll : rolls) {
            sum1 += roll;
        }
        int sum2 = total - sum1;
        if (sum2 < n || sum2 > n * 6) {
            return new int[0];
        }
        int avg = sum2 / n;
        int[] ans = new int[n];
        Arrays.fill(ans, avg);
        int rem = sum2 - avg * n;
        for (int i = 0; i < rem; i++) {
            ans[i]++;
        }
        return ans;
    }
}
