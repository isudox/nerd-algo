package com.leetcode;

import java.util.Arrays;

/**
 * 377. Combination Sum IV
 * https://leetcode.com/problems/combination-sum-iv/
 *
 * Given an array of distinct integers nums and a target integer target, return
 * the number of possible combinations that add up to target.
 *
 * The answer is guaranteed to fit in a 32-bit integer.
 *
 * Example 1:
 *
 * Input: nums = [1,2,3], target = 4
 * Output: 7
 * Explanation:
 * The possible combination ways are:
 * (1, 1, 1, 1)
 * (1, 1, 2)
 * (1, 2, 1)
 * (1, 3)
 * (2, 1, 1)
 * (2, 2)
 * (3, 1)
 * Note that different sequences are counted as different combinations.
 *
 * Example 2:
 *
 * Input: nums = [9], target = 3
 * Output: 0
 *
 * Constraints:
 *
 * 1 <= nums.length <= 200
 * 1 <= nums[i] <= 1000
 * All the elements of nums are unique.
 * 1 <= target <= 1000
 *
 * Follow up: What if negative numbers are allowed in the given array? How does
 * it change the problem? What limitation we need to add to the question to
 * allow negative numbers?
 */
public class Problem377 {
    public int combinationSum(int[] nums, int target) {
        Arrays.sort(nums);
        if (nums[0] > target)
            return 0;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int i = nums[0]; i < target + 1; i++) {
            for (int num : nums) {
                if (num > i) {
                    break;
                }
                dp[i] += dp[i - num];
            }
        }
        return dp[target];
    }
}
