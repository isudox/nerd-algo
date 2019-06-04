package com.leetcode;

/**
 * 34. Find First and Last Position of Element in Sorted Array
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
 *
 * Given an array of integers nums sorted in ascending order,
 * find the starting and ending position of a given target value.
 *
 * Your algorithm's runtime complexity must be in the order of O(log n).
 *
 * If the target is not found in the array, return [-1, -1].
 *
 * Example 1:
 *
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 *
 * Example 2:
 *
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 */
public class FindFirstAndLastPositionOfElementInSortedArray {

    public int[] searchRange(int[] nums, int target) {
        int size = nums.length, lo = 0, hi = size - 1, p = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] < target) {
                lo = mid + 1;
                continue;
            }
            if (nums[mid] > target) {
                hi = mid - 1;
                continue;
            }
            if (nums[mid] == target) {
                p = mid;
                break;
            }
        }

        int left = p, right = p;

        if (p > -1) {
            while (right < size && nums[right] == target) right++;
            while (left >= 0 && nums[left] == target) left--;
            right--;
            left++;
        }

        return new int[]{left, right};
    }
}
