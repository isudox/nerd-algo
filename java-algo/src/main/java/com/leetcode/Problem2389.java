package com.leetcode;

import java.util.Arrays;

/**
 * 2389. Longest Subsequence With Limited Sum
 * https://leetcode.com/problems/longest-subsequence-with-limited-sum/
 */
public class Problem2389 {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            ans[i] = helper(nums, queries[i]);
        }
        return ans;
    }

    private int helper(int[] nums, int q) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >> 1;
            if (nums[mid] > q) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
