package com.leetcode;

/**
 * 2444. Count Subarrays With Fixed Bounds
 * https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
 */
public class Problem2444 {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long ans = 0;
        int minIdx = -1, maxIdx = -1, x = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == minK) {
                minIdx = i;
            }
            if (nums[i] == maxK) {
                maxIdx = i;
            }
            if (nums[i] < minK || nums[i] > maxK) {
                x = i;
            }
            ans += Math.max(Math.min(minIdx, maxIdx) - x, 0);
        }
        return ans;
    }
}
