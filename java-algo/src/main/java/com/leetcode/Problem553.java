package com.leetcode;

/**
 * 553. Optimal Division
 * https://leetcode.com/problems/optimal-division/
 */
public class Problem553 {
    public String optimalDivision(int[] nums) {
        int n = nums.length;
        String ans = String.valueOf(nums[0]);
        String suffix = "";
        for (int i = 1; i < n; i++) {
            suffix += String.valueOf(nums[i]);
            if (i < n - 1) {
                suffix += "/";
            }
        }
        if (n > 2) {
            suffix = "(" + suffix + ")";
        }
        return suffix.equals("") ? ans : ans + "/" + suffix;
    }
}
