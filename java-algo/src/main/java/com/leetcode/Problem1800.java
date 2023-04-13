package com.leetcode;

/**
 * 1800. Maximum Ascending Subarray Sum
 * https://leetcode.com/problems/maximum-ascending-subarray-sum/
 */
public class Problem1800 {
    public int maxAscendingSum(int[] nums) {
        int ans = 0, sum = 0, pre = 0;
        for (int num : nums) {
            if (num <= pre) {
                if (sum > ans) {
                    ans = sum;
                }
                sum = num;
                pre = num;
            } else {
                pre = num;
                sum += num;
                if (sum > ans) {
                    ans = sum;
                }
            }
        }
        return ans;
    }
}
