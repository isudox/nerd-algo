package com.leetcode;

import java.util.Arrays;

/**
 * 179. Largest Number
 * https://leetcode.com/problems/largest-number/description/
 *
 * Given a list of non-negative integers nums, arrange them such that
 * they form the largest number.
 *
 * Note: The result may be very large, so you need to return a string
 * instead of an integer.
 *
 * Example 1:
 *
 * Input: nums = [10,2]
 * Output: "210"
 *
 * Example 2:
 *
 * Input: nums = [3,30,34,5,9]
 * Output: "9534330"
 *
 * Example 3:
 *
 * Input: nums = [1]
 * Output: "1"
 *
 * Example 4:
 *
 * Input: nums = [10]
 * Output: "10"
 *
 * Constraints:
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 10^9
 */
class Problem179 {
    public String largestNumber(int[] nums) {
        String[] strings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strings[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(strings, (o1, o2) -> {
            long x = Long.parseLong(o1 + o2);
            long y = Long.parseLong(o2 + o1);
            return (int) (y - x);
        });
        if ("0".equals(strings[0]))
            return "0";
        return String.join("", strings);
    }
}
