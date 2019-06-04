package com.leetcode;

/**
 * 53. Maximum Subarray
 * https://leetcode.com/problems/maximum-subarray/
 *
 * Given an integer array nums, find the contiguous subarray (containing at
 * least one number) which has the largest sum and return its sum.
 *
 * Example:
 *
 *   Input: [-2,1,-3,4,-1,2,1,-5,4],
 *   Output: 6
 *   Explanation: [4,-1,2,1] has the largest sum = 6.
 *
 * Follow up:
 *
 * If you have figured out the O(n) solution, try coding another solution using
 * the divide and conquer approach, which is more subtle.
 */
public class MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int len = nums.length;
        assert len > 0;
        int maxSum = nums[0];
        int curSum = nums[0];

        for (int i = 1; i < len; i++) {
            if (curSum <= 0) {
                curSum = nums[i];
            } else {
                curSum += nums[i];
            }
            maxSum = Math.max(maxSum, curSum);
        }

        return maxSum;
    }

    /**
     * Brute force approach by for-loop.
     * O(n^2), not acceptable.
     * @param nums
     * @return
     */
    public int bruteForce(int[] nums) {
        int max = nums[0];
        int size = nums.length;
        for (int i = 0; i < size; i++) {
            for (int j = i; j < size; j++) {
                int temp = sumArray(nums, i, j);
                if (temp > max) {
                    max = temp;
                }
            }
        }
        return max;
    }

    private int sumArray(int[] nums, int left, int right) {
        int sum = 0;
        for (int i = left; i <= right; i++) {
            sum += nums[i];
        }
        return sum;
    }
}
