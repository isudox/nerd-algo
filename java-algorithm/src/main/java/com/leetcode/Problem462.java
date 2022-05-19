package com.leetcode;

import java.util.Arrays;

/**
 * 462. Minimum Moves to Equal Array Elements II
 * https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
 */
public class Problem462 {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int ans = 0, i = 0, j = nums.length - 1;
        while (i < j) {
            ans += nums[j--] - nums[i++];
        }
        return ans;
    }
}
