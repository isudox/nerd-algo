package com.leetcode;

/**
 * 912. Sort an Array
 * https://leetcode.com/problems/sort-an-array/
 */
public class Problem912 {
    public int[] sortArray(int[] nums) {
        insertSort(nums);
        return nums;
    }

    private void insertSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            for (int j = i; j >= 1; j--) {
                if (nums[j] >= nums[j - 1]) {
                    break;
                }
                swap(nums, j, j - 1);
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
