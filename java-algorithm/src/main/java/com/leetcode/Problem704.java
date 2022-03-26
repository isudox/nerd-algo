package com.leetcode;

/**
 * 704. Binary Search
 * https://leetcode.com/problems/binary-search/
 */
public class Problem704 {
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length - 1, mid;
        while (i <= j) {
            mid = (j - i) / 2 + i;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target)
                i = mid + 1;
            else
                j = mid - 1;
        }
        return -1;
    }
}
