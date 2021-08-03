package com.leetcode;

/**
 * 137. Single Number II
 * https://leetcode.com/problems/single-number-ii/
 *
 * Given an integer array nums where every element appears three times except
 * for one, which appears exactly once. Find the single element and return it.
 *
 * Example 1:
 * Input: nums = [2,2,3,2]
 * Output: 3
 * Example 2:
 * Input: nums = [0,1,0,1,0,1,99]
 * Output: 99
 *
 * Constraints:
 *
 * 1 <= nums.length <= 3 * 10^4
 * -2^31 <= nums[i] <= 2^31 - 1
 * Each element in nums appears exactly three times except for one element
 * which appears once.
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
