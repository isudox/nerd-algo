package com.leetcode;

/**
 * 334. Increasing Triplet Subsequence
 * https://leetcode.com/problems/increasing-triplet-subsequence/
 * Constraints:
 *   1 <= nums.length <= 5 * 10^5
 *   -2^31 <= nums[i] <= 2^31 - 1
 */
public class Problem334 {
    public boolean increasingTriplet(int[] nums) {
        int n = nums.length;
        if (n < 3) {
            return false;
        }
        int[] leftMin = new int[n];
        int[] rightMax = new int[n];
        leftMin[0] = nums[0];
        rightMax[n - 1] = nums[n - 1];
        for (int i = 1; i < n; i++) {
            leftMin[i] = Math.min(leftMin[i - 1], nums[i]);
        }
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], nums[i]);
        }
        for (int i = 1; i < n - 1; i++) {
            if (leftMin[i - 1] < nums[i] && nums[i] < rightMax[i + 1]) {
                return true;
            }
        }
        return false;
    }
}
