package com.leetcode;

/**
 * 2016. Maximum Difference Between Increasing Elements
 * https://leetcode.com/problems/maximum-difference-between-increasing-elements/
 */
public class Problem2016 {
    public int maximumDifference(int[] nums) {
        int ans = -1;
        int min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < min) {
                min = nums[i];
            } else if (nums[i] > min) {
                ans = Math.max(ans, nums[i] - min);
            }
        }
        return ans;
    }
}
