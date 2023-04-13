package com.leetcode;

import java.util.Arrays;

/**
 * 1818. Minimum Absolute Sum Difference
 * https://leetcode.com/problems/minimum-absolute-sum-difference/
 */
public class Problem1818 {
    public int minAbsoluteSumDiff(int[] nums1, int[] nums2) {
        int total = 0, maxn = 0, mod = (int) 1e9 + 7;
        int[] sortedNums1 = Arrays.copyOf(nums1, nums1.length);
        Arrays.sort(sortedNums1);
        for (int i = 0; i < nums1.length; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            if (diff == 0)
                continue;
            total = (total + diff) % mod;
            int j = bs(sortedNums1, nums2[i]);
            if (j < nums1.length) {
                maxn = Math.max(maxn, diff - (sortedNums1[j] - nums2[i]));
            }
            if (j > 0) {
                maxn = Math.max(maxn, diff - (nums2[i] - sortedNums1[j - 1]));
            }
        }
        return (total - maxn + mod) % mod;
    }

    private int bs(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        if (target > nums[hi]) {
            return hi + 1;
        }
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
