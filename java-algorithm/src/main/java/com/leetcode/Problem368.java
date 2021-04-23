package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 368. Largest Divisible Subset
 * https://leetcode.com/problems/largest-divisible-subset/
 *
 * Given a set of distinct positive integers nums, return the largest subset
 * answer such that every pair (answer[i], answer[j]) of elements in this subset
 * satisfies:
 *
 * answer[i] % answer[j] == 0, or
 * answer[j] % answer[i] == 0
 *
 * If there are multiple solutions, return any of them.
 *
 * Example 1:
 *
 * Input: nums = [1,2,3]
 * Output: [1,2]
 * Explanation: [1,3] is also accepted.
 *
 * Example 2:
 *
 * Input: nums = [1,2,4,8]
 * Output: [1,2,4,8]
 *
 * Constraints:
 *
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= 2 * 10^9
 * All the integers in nums are unique.
 */
public class Problem368 {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }
        int maxLen = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    maxLen = Math.max(dp[i], maxLen);
                }
            }
        }
        List<Integer> ans = new ArrayList<>(maxLen);
        for (int i = 0, m = maxLen; i < m; i++) {
            helper(nums, dp, maxLen--, ans);
        }
        return ans;
    }

    private void helper(int[] nums, int[] dp, int target, List<Integer> ans) {
        for (int i = dp.length - 1; i >= 0; i--) {
            if (dp[i] == target) {
                if (ans.isEmpty() || ans.get(0) % nums[i] == 0) {
                    ans.add(0, nums[i]);
                }
            }
        }
    }
}
