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
 *   Explanation: [4,-1,2,1] has the largest sum = 6.
 *
 * Follow up:
 *
 * If you have figured out the O(n) solution, try coding another solution using
 * the divide and conquer approach, which is more subtle.
 */
public class Problem53 {

    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int curSum = nums[0];
        for (int i = 1; i < nums.length; i++) {
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
     * Prefix Sum.
     */
    public int maxSubArray2(int[] nums) {
        for (int i = 1; i < nums.length; i++)
            nums[i] += nums[i - 1];
        int ans = nums[0], min = 0;
        for (int num : nums) {
            ans = Math.max(ans, num - min);
            min = Math.min(min, num);
        }
        return ans;
    }

    public int maxSubArray3(int[] nums) {
        int ans = nums[0], min = 0, sum = 0;
        for (int num : nums) {
            sum += num;
            ans = Math.max(ans, sum - min);
            min = Math.min(min, sum);
        }
        return ans;
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
