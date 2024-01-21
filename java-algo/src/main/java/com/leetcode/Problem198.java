package com.leetcode;

/**
 * 198. House Robber
 * https://leetcode.com/problems/house-robber/
 */
public class Problem198 {
    public int rob(int[] nums) {
        int x = 0, y = nums[0];  // x: skip current num; y: pick current num
        for (int i = 1; i < nums.length; i++) {
            int tmpX = Math.max(x, y);
            int tmpY = x + nums[i];
            x = tmpX;
            y = tmpY;
        }
        return Math.max(x, y);
    }
}
