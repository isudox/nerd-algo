package com.leetcode;

import java.util.Arrays;

/**
 * 189. Rotate Array
 * https://leetcode.com/problems/rotate-array/
 */
public class Problem189 {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        if (k == 0) {
            return;
        }
        int[] left = Arrays.copyOfRange(nums, 0, n - k);
        int[] right = Arrays.copyOfRange(nums, n - k, n);
        for (int i = 0; i < right.length; i++) {
            nums[i] = right[i];
        }
        for (int i = 0; i < left.length; i++) {
            nums[k + i] = left[i];
        }
    }
}
