package com.leetcode;

import java.util.Arrays;

/**
 * 908. Smallest Range I
 * https://leetcode.com/problems/smallest-range-i/
 */
public class Problem908 {
    public int smallestRangeI(int[] nums, int k) {
        if (nums.length == 1) {
            return 0;
        }
        Arrays.sort(nums);
        int min = nums[0], max = nums[nums.length - 1];
        if (max - min <= 2 * k) {
            return 0;
        }
        return max - min - 2 * k;
    }
}
