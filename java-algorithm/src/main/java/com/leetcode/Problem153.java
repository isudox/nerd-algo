package com.leetcode;

/**
 * 153. Find Minimum in Rotated Sorted Array
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 */
public class Problem153 {
    public int findMin(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1])
                return nums[i];
        }
        return nums[0];
    }

    public int findMin2(int[] nums) {
        int lo = 0, hi = nums.length - 1, mid = 0;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (nums[mid] < nums[hi])
                hi = mid;
            else
                lo = mid + 1;
        }
        return nums[lo];
    }
}
