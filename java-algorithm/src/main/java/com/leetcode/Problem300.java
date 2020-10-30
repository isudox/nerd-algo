package com.leetcode;

/**
 * 300. Longest Increasing Subsequence
 * https://leetcode.com/problems/longest-increasing-subsequence/
 *
 * Given an unsorted array of integers, find the length of longest increasing
 * subsequence.
 *
 * Example:
 *
 * Input: [10,9,2,5,3,7,101,18]
 * Output: 4
 * Explanation: The longest increasing subsequence is [2,3,7,101],
 * therefore the length is 4.
 *
 * Note:
 *
 * There may be more than one LIS combination, it is only necessary for you
 * to return the length.
 * Your algorithm should run in O(n^2) complexity.
 *
 * Follow up: Could you improve it to O(n log n) time complexity?
 */
public class Problem300 {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];  // dp[i] = max length of LIS which last num is nums[i]
        int ans = 0;
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            ans = Math.max(ans, dp[i]);
        }
        return ans;
    }
}
