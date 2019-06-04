package com.leetcode;

import java.util.Arrays;

/**
 * 136. Single Number
 * https://leetcode.com/problems/single-number/
 *
 * Given a non-empty array of integers, every element appears twice
 * except for one. Find that single one.
 *
 * Note:
 *
 *   Your algorithm should have a linear runtime complexity.
 *   Could you implement it without using extra memory?
 *
 * Example 1:
 *
 *   Input: [2,2,1]
 *   Output: 1
 *
 * Example 2:
 *
 *   Input: [4,1,2,1,2]
 *   Output: 4
 */
public class SingleNumber {

    public int singleNumber(int[] nums) {
        Arrays.sort(nums);

        int i = 0;
        while (i < nums.length) {
            if (i == nums.length - 1) {
                break;
            }
            if (nums[i] == nums[i + 1]) {
                i += 2;
            } else {
                break;
            }
        }

        return nums[i];
    }

    public int reduce(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[0] ^= nums[i];
        }
        return nums[0];
    }
}
