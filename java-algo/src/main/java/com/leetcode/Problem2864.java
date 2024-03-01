package com.leetcode;

/**
 * https://leetcode.com/problems/maximum-odd-binary-number/
 */
public class Problem2864 {
    public String maximumOddBinaryNumber(String s) {
        int[] count = new int[2];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - '0']++;
        }
        return "1".repeat(count[1] - 1) + "0".repeat(count[0]) + "1";
    }
}
