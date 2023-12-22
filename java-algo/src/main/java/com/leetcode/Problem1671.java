package com.leetcode;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array
 */
public class Problem1671 {
    public int minimumMountainRemovals(int[] nums) {
	    int n = nums.length;
        int[] pre = getLis(nums);
        int[] rev = reverse(nums);
        int[] suf = getLis(rev);
        suf = reverse(suf);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (pre[i] > 1 && suf[i] > 1) {
                ans = Math.max(ans, pre[i] + suf[i] - 1);
            }
        }
        return n - ans;
    }

    private int[] getLis(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        return dp;
    }

    private int[] reverse(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        for (int i = 0; i < n; i++) {
            ret[n - 1 - i] = nums[i];
        }
        return ret;
    }
}
