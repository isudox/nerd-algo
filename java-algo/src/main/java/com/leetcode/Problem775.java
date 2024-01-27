package com.leetcode;

/**
 * 775. Global and Local Inversions
 * https://leetcode.com/problems/global-and-local-inversions/
 */
public class Problem775 {
    public boolean isIdealPermutation(int[] nums) {
        int n = nums.length;
        if (n < 3) {
            return true;
        }
        int maxIdx = 0;
        for (int i = 2; i < n; i++) {
            if (nums[i] < nums[maxIdx]) {
                return false;
            }
            if (nums[i - 1] > nums[maxIdx]) {
                maxIdx = i - 1;
            }
        }
        return true;
    }
}
