package com.leetcode;

/**
 * 540. Single Element in a Sorted Array
 * https://leetcode.com/problems/single-element-in-a-sorted-array/
 */
public class Problem540 {
    public int singleNonDuplicate(int[] nums) {
        int i = 0, j = nums.length - 1;
        while (i < j) {
            int mid = i + (j - i) / 2;
            if (mid % 2 == 0) {
                if (mid > 0 && nums[mid] == nums[mid - 1]) {
                    j = mid - 2;
                } else if (mid < nums.length - 1 && nums[mid] == nums[mid + 1]) {
                    i = mid + 2;
                } else {
                    return nums[mid];
                }
            } else {
                if (nums[mid] == nums[mid - 1]) {
                    i = mid + 1;
                } else if (mid < nums.length - 1 && nums[mid] == nums[mid + 1]) {
                    j = mid - 1;
                } else {
                    return nums[mid];
                }
            }
        }
        return nums[i];
    }
}
