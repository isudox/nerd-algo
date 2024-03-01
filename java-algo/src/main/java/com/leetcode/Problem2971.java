package com.leetcode;

import java.util.Arrays;

/**
 * 2971. Find Polygon With the Largest Perimeter
 * https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
 */
public class Problem2971 {
    public long largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        long[] preSum = new long[nums.length];
        preSum[0] = nums[0];
        long ans = -1;
        for (int i = 1; i < nums.length; i++) {
            preSum[i] += preSum[i - 1] + nums[i];
            if (preSum[i - 1] > nums[i]) {
                ans = preSum[i];
            }
        }
        return ans;
    }
}
