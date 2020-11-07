package com.leetcode;

/**
 * 941. Valid Mountain Array
 * https://leetcode.com/problems/valid-mountain-array/
 *
 * Given an array A of integers, return true if and only if it is a valid mountain array.
 *
 * Recall that A is a mountain array if and only if:
 *
 * A.length >= 3
 * There exists some i with 0 < i < A.length - 1 such that:
 * A[0] < A[1] < ... A[i-1] < A[i]
 * A[i] > A[i+1] > ... > A[A.length - 1]
 *
 * Example 1:
 *
 * Input: [2,1]
 * Output: false
 *
 * Example 2:
 *
 * Input: [3,5,5]
 * Output: false
 *
 * Example 3:
 *
 * Input: [0,3,2,1]
 * Output: true
 *
 * Note:
 *
 * 0 <= A.length <= 10000
 * 0 <= A[i] <= 10000
 */
public class Problem941 {
    public boolean validMountainArray(int[] nums) {
        int n = nums.length;
        if (n < 3) return false;
        if (nums[0] >= nums[1]) return false;
        boolean foundPeak = false;
        for (int i = 0; i < n - 1; i++) {
            if (!foundPeak) {
                if (nums[i] == nums[i + 1]) return false;
                if (nums[i] > nums[i + 1]) foundPeak = true;
            } else {
                if (nums[i] <= nums[i + 1]) return false;
            }
        }
        return foundPeak;
    }

    // double-pointer
    public boolean validMountainArray1(int[] nums) {
        int n = nums.length;
        int i = 0, j = n - 1;
        while (i < n - 1 && nums[i] < nums[i + 1])
            i++;
        while (j > 0 && nums[j] < nums[j - 1])
            j--;
        return i == j && i != 0 && i != n - 1;
    }
}
