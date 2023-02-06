package com.leetcode;

/**
 * 1470. Shuffle the Array
 * https://leetcode.com/problems/shuffle-the-array/
 */
public class Problem1470 {
    public int[] shuffle(int[] nums, int n) {
        int[] ans = new int[2 * n];
        int left = 0, right = n;
        for (int i = 0; i < ans.length; i++) {
            ans[i] = i % 2 == 0 ? nums[left++] : nums[right++];
        }
        return ans;
    }
}
