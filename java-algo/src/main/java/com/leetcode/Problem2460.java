package com.leetcode;

public class Problem2460 {
    public int[] applyOperations(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        int[] ans = new int[nums.length];
        int i = 0;
        for (int num : nums) {
            if (num != 0) {
                ans[i++] = num;
            }
        }
        return ans;
    }
}
