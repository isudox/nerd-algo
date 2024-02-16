package com.leetcode;

import java.util.*;

/**
 * 368. Largest Divisible Subset
 * https://leetcode.com/problems/largest-divisible-subset/
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

    public List<Integer> largestDivisibleSubset2(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        List<Integer>[] dp = new List[n];
        for (int i = 0; i < n; i++) {
            dp[i] = new ArrayList<>();
            dp[i].add(nums[i]);
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] > 0) {
                    continue;
                }
                if (nums[j] > nums[i] / 2) {
                    break;
                }
                if (dp[j].size() + 1 > dp[i].size()) {
                    dp[i] = new ArrayList<>(dp[j]);
                    dp[i].add(nums[i]);
                }
            }
            if (dp[i].size() > ans.size()) {
                ans = dp[i];
            }
        }
        return ans;
    }
}
