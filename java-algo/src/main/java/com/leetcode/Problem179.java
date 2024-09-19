package com.leetcode;

import java.util.Arrays;

/**
 * 179. Largest Number
 * https://leetcode.com/problems/largest-number/description/
 */
class Problem179 {
    public String largestNumber(int[] nums) {
        String[] numStrings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numStrings[i] = Integer.toString(nums[i]);
        }
        Arrays.sort(numStrings, (a, b) -> (b + a).compareTo(a + b));
        if (numStrings[0].equals("0")) {
            return "0";
        }
        return String.join("", numStrings);
    }
}
