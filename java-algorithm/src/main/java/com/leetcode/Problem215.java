package com.leetcode;

import java.util.*;

/**
 * 215.
 */
class Problem215 {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}
