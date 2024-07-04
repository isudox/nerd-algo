package com.leetcode;

import java.util.Arrays;

/**
 * 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
 * https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
 */
public class Problem1509 {
    public int minDifference(int[] nums) {
        int n = nums.length;
        if (n <= 4) {
            return 0;
        }
        Arrays.sort(nums);
        int ans = nums[n - 1] - nums[0];
        for (int i = 0, j = n - 4; i < 4; i++, j++) {
            ans = Math.min(ans, nums[j] - nums[i]);
        }
        return ans;
    }
}
