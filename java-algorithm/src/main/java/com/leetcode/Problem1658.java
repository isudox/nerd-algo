package com.leetcode;

/**
 * 1658. Minimum Operations to Reduce X to Zero
 * https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
 */
public class Problem1658 {
    // TLE
    public int minOperations(int[] nums, int x) {
        int ans = dfs(nums, 0, nums.length - 1, x);
        return ans < Integer.MAX_VALUE ? ans : -1;
    }

    private int dfs(int[] nums, int i, int j, int target) {
        if (target == 0) {
            return 0;
        }
        if (target < 0) {
            return Integer.MAX_VALUE;
        }
        if (i > j) {
            return Integer.MAX_VALUE;
        }
        if (target < nums[i] && target < nums[j]) {
            return Integer.MAX_VALUE;
        }
        int ret = Math.min(dfs(nums, i + 1, j, target - nums[i]), dfs(nums, i, j - 1, target - nums[j]));
        return ret < Integer.MAX_VALUE ? ret + 1 : Integer.MAX_VALUE;
    }

    public int minOperations2(int[] nums, int x) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        if (total < x) {
            return -1;
        }
        int diff = total - x;
        int i = 0, j = 0;
        int windowSum = 0;
        int windowSize = -1;
        while (j < nums.length) {
            windowSum += nums[j];
            while (windowSum > diff) {
                windowSum -= nums[i++];
            }
            if (windowSum == diff) {
                windowSize = Math.max(windowSize, j - i + 1);
            }
            j++;
        }
        return windowSize == -1 ? -1 : nums.length - windowSize;
    }
}
