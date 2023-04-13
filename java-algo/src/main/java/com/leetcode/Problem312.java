package com.leetcode;

/**
 * 312. Burst Balloons
 * https://leetcode.com/problems/burst-balloons/
 *
 * Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
 * on it represented by array nums. You are asked to burst all the balloons.
 * If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
 * Here left and right are adjacent indices of i.
 * After the burst, the left and right then becomes adjacent.
 *
 * Find the maximum coins you can collect by bursting the balloons wisely.
 *
 * Note:
 *
 * You may imagine nums[-1] = nums[n] = 1.
 * They are not real therefore you can not burst them.
 * 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
 * Example:
 *
 * Input: [3,1,5,8]
 * Output: 167
 * Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
 *              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
 */
public class Problem312 {

    public int maxCoins(int[] nums) {
        int n = nums.length;
        int[] newNums = new int[n + 2];
        for (int i = 1; i <= n; i++)
            newNums[i] = nums[i - 1];
        newNums[0] = 1;
        newNums[n + 1] = 1;
        int[][] memo = new int[n + 2][n + 2];
        return burst(newNums, memo, 0, n + 1);
    }

    private int burst(int[] arr, int[][] memo, int left, int right) {
        if (left + 1 == right)
            return 0;
        if (memo[left][right] != 0)
            return memo[left][right];
        int max = 0;
        for (int i = left + 1; i < right; i++) {
            max = Math.max(arr[left] * arr[i] * arr[right] +
                    burst(arr, memo, left, i) +
                    burst(arr, memo, i, right), max);
        }
        memo[left][right] = max;
        return max;
    }
}
