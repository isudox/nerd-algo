package com.leetcode.solution;

/**
 * 35. Search Insert Position
 * https://leetcode.com/problems/search-insert-position/
 * <p>
 * Given a sorted array and a target value, return the index if the target
 * is found.
 * If not, return the index where it would be if it were inserted in order.
 * <p>
 * You may assume no duplicates in the array.
 * <p>
 * Example 1:
 * <p>
 * Input: [1,3,5,6], 5
 * Output: 2
 * <p>
 * Example 2:
 * <p>
 * Input: [1,3,5,6], 2
 * Output: 1
 * <p>
 * Example 3:
 * <p>
 * Input: [1,3,5,6], 7
 * Output: 4
 * <p>
 * Example 4:
 * <p>
 * Input: [1,3,5,6], 0
 * Output: 0
 */
public class SearchInsertPosition {

    public int searchInsert(int[] nums, int target) {
        int size = nums.length;
        for (int i = 0; i < size; i++) {
            if (nums[i] == target) return i;
            if (nums[i] > target && i == 0) return 0;
            if (nums[i] < target && i == size - 1) return size;
            if (nums[i] < target && nums[i + 1] > target) return i + 1;
        }
        return 0;
    }
}
