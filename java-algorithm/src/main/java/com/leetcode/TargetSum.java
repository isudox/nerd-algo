package com.leetcode;

import java.util.Arrays;

/**
 * 494. Target Sum
 * https://leetcode.com/problems/target-sum/
 *
 * You are given a list of non-negative integers, a1, a2, ..., an, and a target,
 * S. Now you have 2 symbols + and -. For each integer, you should choose one
 * from + and - as its new symbol.
 * ⁠
 *
 * Find out how many ways to assign symbols to make sum of integers equal to
 * target S.
 *
 *
 * Example 1:
 *
 * Input: nums is [1, 1, 1, 1, 1], S is 3.
 * Output: 5
 * Explanation:
 *
 * -1+1+1+1+1 = 3
 * +1-1+1+1+1 = 3
 * +1+1-1+1+1 = 3
 * +1+1+1-1+1 = 3
 * +1+1+1+1-1 = 3
 *
 * There are 5 ways to assign symbols to make the sum of nums be target 3.
 *
 *
 * Note:
 *
 * The length of the given array is positive and will not exceed 20.
 * The sum of elements in the given array will not exceed 1000.
 * Your output answer is guaranteed to be fitted in a 32-bit integer.
 */
public class TargetSum {

    /**
     * Time Complexity: O(2^n)
     * Space Complexity: O(n)
     */
    public int findTargetSumWays(int[] nums, int s) {
        int length = nums.length;
        if (length == 0)
            return s == 0 ? 1 : 0;

        int[] nextArr = Arrays.copyOfRange(nums, 1, length);
        return findTargetSumWays(nextArr, s - nums[0]) + findTargetSumWays(nextArr, s + nums[0]);
    }

    public int findTargetSumWays2(int[] nums, int s) {
        int length = nums.length;
        int[][] store = new int[length][2001];
        for (int[] row : store) {
            Arrays.fill(row, Integer.MIN_VALUE);
        }

        return 0;
    }

}
