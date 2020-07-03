package com.leetcode;

/**
 * 45. Jump Game II
 * https://leetcode.com/problems/jump-game-ii/
 *
 * Given an array of non-negative integers, you are initially positioned
 * at the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that position.
 *
 * Your goal is to reach the last index in the minimum number of jumps.
 *
 * Example:
 *
 * Input: [2,3,1,1,4]
 * Output: 2
 * Explanation: The minimum number of jumps to reach the last index is 2.
 *     Jump 1 step from index 0 to 1, then 3 steps to the last index.
 * Note:
 *
 * You can assume that you can always reach the last index.
 */
public class Problem45 {

    public int jump(int[] nums) {
        int size = nums.length;
        if (size < 2)
            return 0;
        int[] memo = new int[size];
        for (int i = 0; i < size; i++)
            memo[i] = size;
        try_jump(0, 0, nums, memo);
        return memo[size - 1];
    }

    private void try_jump(int i, int pre_steps, int[] nums, int[] memo) {
        if (i == nums.length - 1)
            return;
        for (int j = nums[i]; j >= 0; j--) {
            int k = Math.min(i + j, nums.length - 1);
            if (memo[k] < nums.length) {
                if (pre_steps + 1 < memo[k]) {
                    memo[k] = Math.min(pre_steps + 1, memo[k]);
                    try_jump(k, pre_steps + 1, nums, memo);
                }
            } else {
                memo[k] = pre_steps + 1;
                try_jump(k, pre_steps + 1, nums, memo);
            }
        }
    }
}
