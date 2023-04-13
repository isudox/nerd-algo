package com.leetcode;

/**
 * 268. Missing Number
 * https://leetcode.com/problems/missing-number/
 */
public class Problem268 {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = n * (n + 1) / 2;
        for (int num : nums) {
            sum -= num;
        }
        return sum;
    }
}
