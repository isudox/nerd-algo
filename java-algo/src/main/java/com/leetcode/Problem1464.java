package com.leetcode;

import java.util.Arrays;

/**
 * 1464. Maximum Product of Two Elements in an Array
 */
public class Problem1464 {
    public int maxProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        return (nums[n - 1] - 1) * (nums[n - 2] - 1);
    }
}
