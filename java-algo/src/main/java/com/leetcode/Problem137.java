package com.leetcode;

/**
 * 137. Single Number II
 * https://leetcode.com/problems/single-number-ii/
 *
 * Follow up: Your algorithm should have a linear runtime complexity.
 * Could you implement it without using extra memory?
 */
public class Problem137 {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int count = 0;
            for (int num : nums) {
                // count the `1` of ith from the binary of all the nums.
                count += ((num >> i) & 1);
            }
            if (count % 3 != 0) {
                ans |= (1 << i);
            }
        }
        return ans;
    }
}
