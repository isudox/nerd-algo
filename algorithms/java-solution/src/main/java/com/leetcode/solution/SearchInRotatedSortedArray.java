package com.leetcode.solution;

/**
 * 33. Search in Rotated Sorted Array
 * https://leetcode.com/problems/search-in-rotated-sorted-array/
 * <p>
 * Suppose an array sorted in ascending order is rotated at some pivot unknown
 * to you beforehand.
 * <p>
 * (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
 * <p>
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 * <p>
 * You may assume no duplicate exists in the array.
 * <p>
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * <p>
 * Example 1:
 * <p>
 * Input: nums = [4,5,6,7,0,1,2], target = 0
 * Output: 4
 * <p>
 * Example 2:
 * <p>
 * Input: nums = [4,5,6,7,0,1,2], target = 3
 * Output: -1
 */
public class SearchInRotatedSortedArray {

    /**
     * Not satisfied with the runtime complexity of O(log n), actually O(n).
     */
    public int search1(int[] nums, int target) {
        int size = nums.length;
        for (int i = 0; i < size; i++) {
            if (nums[i] == target) {
                return i;
            }
        }

        return -1;
    }

    /**
     * Binary search.
     */
    public int search2(int[] nums, int target) {
        int size = nums.length, low = 0, high = size - 1;

        while (low < high) {
            int mid = (low + high) / 2;
            if (nums[mid] > nums[high]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        int rotated = low;
        low = 0;
        high = size - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            // [4, 5, 6, 7, 0, 1, 2] => [4, 5, 6, 7, 0, 1, 2, [4, 5, 6, 7]]
            int virtualMid = (mid + rotated) % size;
            if (nums[virtualMid] == target) {
                return virtualMid;
            }
            if (nums[virtualMid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return -1;
    }
}
