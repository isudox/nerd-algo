package com.leetcode;

import java.util.Arrays;

public class Problem1913 {
    public int maxProductDifference(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        return nums[n - 1] * nums[n - 2] - nums[0] * nums[1];
    }
}
