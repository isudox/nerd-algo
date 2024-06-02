package com.leetcode;

import java.util.Arrays;

/**
 * 1608. Special Array With X Elements Greater Than or Equal X
 * https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
 */
public class Problem1608 {
    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int lo = 0, hi = Math.min(nums.length, nums[nums.length - 1]);
        Arrays.binarySearch(nums, lo);
        while (lo <= hi) {
            int mid = (lo + hi) >> 1;
            int pos = search(nums, mid);
            int cnt = nums.length - pos;
            if (cnt == mid) return mid;
            if (cnt < mid) hi = mid - 1;
            else lo = mid + 1;
        }
        return -1;
    }

    private int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (nums[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        return nums[lo] >= target ? lo : nums.length;
    }
}
