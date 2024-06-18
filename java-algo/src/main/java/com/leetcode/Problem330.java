package com.leetcode;

/**
 * 330. Patching Array
 * https://leetcode.com/problems/patching-array/
 */
public class Problem330 {
    public int minPatches(int[] nums, int n) {
        int ans = 0;
        int i = 0, sz = nums.length;
        long x = 1;
        while (x <= n) {
            if (i < sz && nums[i] <= x) {
                x += nums[i++];
            } else {
                x <<= 1;
                ans++;
            }
        }
        return ans;
    }
}
