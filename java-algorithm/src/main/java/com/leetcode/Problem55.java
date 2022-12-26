package com.leetcode;

/**
 * 55. Jump Game
 * https://leetcode.com/problems/jump-game/description/
 */
public class Problem55 {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n];
        dp[n - 1] = true;
        int next = n - 1;
        for (int i = n - 2; i >= 0; i--) {
            if (i + nums[i] >= next) {
                dp[i] = true;
                next = i;
            } else {
                dp[i] = false;
            }
        }
        return dp[0];
    }
}
