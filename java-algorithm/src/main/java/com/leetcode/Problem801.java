package com.leetcode;

/**
 * 801. Minimum Swaps To Make Sequences Increasing
 * https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/
 */
public class Problem801 {
    public int minSwap(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[] dp0 = new int[n]; // dp0[i] means not swap nums[i]
        int[] dp1 = new int[n]; // dp1[i] means swap nums[i]
        dp1[0] = 1;
        for (int i = 1; i < n; i++) {
            dp0[i] = n;
            dp1[i] = n;
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                // both nums[i-1] and nums[i] not switch
                dp0[i] = Math.min(dp0[i - 1], dp0[i]);
                // both nums[i-1] and nums[i] switch
                dp1[i] = Math.min(dp1[i - 1] + 1, dp1[i]);
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                // nums[i-1] switch, nums[i] not switch
                dp0[i] = Math.min(dp1[i - 1], dp0[i]);
                // nums[i-1] not switch, nums[i] switch
                dp1[i] = Math.min(dp0[i - 1] + 1, dp1[i]);
            }
        }
        return Math.min(dp0[n - 1], dp1[n - 1]);
    }
}
