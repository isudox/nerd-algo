package com.leetcode;

import java.util.Arrays;

/**
 * 3068. Find the Maximum Sum of Node Values
 * https://leetcode.com/problems/find-the-maximum-sum-of-node-values
 */
public class Problem3068 {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        long[][] memo = new long[nums.length][2];
        for (long[] row : memo) {
            Arrays.fill(row, -1);
        }
        return helper(0, 1, nums, k, memo);
    }

    private long helper(int i, int flag, int[] nums, int k, long[][] memo) {
        if (i == nums.length) {
            return flag == 1 ? 0 : Integer.MIN_VALUE;
        }
        if (memo[i][flag] >= 0) {
            return memo[i][flag];
        }
        long a = nums[i] + helper(i + 1, flag, nums, k, memo);
        long b = (nums[i] ^ k) + helper(i + 1, 1 - flag, nums, k, memo);
        return memo[i][flag] = Math.max(a, b);
    }
}
