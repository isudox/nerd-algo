package com.leetcode;

/**
 * 2997. Minimum Number of Operations to Make Array XOR Equal to K
 * https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
 */
public class Problem2997 {
    public int minOperations(int[] nums, int k) {
        for (int num : nums) {
            k ^= num;
        }
        return Integer.bitCount(k);
    }
}
