package com.leetcode;

/**
 * 152. Maximum Product Subarray
 * https://leetcode.com/problems/maximum-product-subarray/
 *
 * Given an integer array nums, find the contiguous subarray within an array
 * (containing at least one number) which has the largest product.
 *
 * Example 1:
 *
 * Input: [2,3,-2,4]
 * Output: 6
 * Explanation: [2,3] has the largest product 6.
 *
 * Example 2:
 *
 * Input: [-2,0,-1]
 * Output: 0
 * Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 */
public class Problem152 {
    public int maxProduct(int[] nums) {
        int ans = nums[0];
        int size = nums.length;
        Integer[][] dp = new Integer[size][3];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < 3; j++)
                dp[i][j] = null;
        }
        if (nums[0] < 0)
            dp[0][0] = nums[0];
        else if (nums[0] == 0)
            dp[0][1] = 0;
        else
            dp[0][2] = nums[0];
        for (int i = 1; i < size; i++) {
            int num = nums[i];
            if (num > 0) {
                if (dp[i - 1][2] != null)
                    dp[i][2] = dp[i - 1][2] * num;
                else
                    dp[i][2] = num;
                if (dp[i - 1][1] != null)
                    dp[i][1] = 0;
                if (dp[i - 1][0] != null)
                    dp[i][0] = dp[i - 1][0] * num;
            }
            if (num < 0) {
                if (dp[i - 1][2] != null)
                    dp[i][0] = dp[i - 1][2] * num;
                else
                    dp[i][0] = num;
                if (dp[i - 1][1] != null)
                    dp[i - 1][1] = 0;
                if (dp[i - 1][0] != null)
                    dp[i][2] = dp[i - 1][0] * num;
            }
            if (num == 0)
                dp[i][1] = 0;
            for (Integer item : dp[i]) {
                if (item != null)
                    ans = Math.max(ans, item);
            }
        }
        return ans;
    }
}
