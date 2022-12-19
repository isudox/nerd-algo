package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 1805. Number of Different Integers in a String
 * https://leetcode.com/problems/number-of-different-integers-in-a-string/
 */
public class Problem1805 {
    public int numDifferentIntegers(String word) {
        Set<String> nums = new HashSet<>();
        int i = 0, n = word.length();
        StringBuilder num = new StringBuilder();
        boolean isNum = false;
        while (i < n) {
            int d = word.charAt(i) - '0';
            if (0 <= d && d <= 9) {
                isNum = true;
                num.append(word.charAt(i));
                if (i == n - 1) {
                    nums.add(convert(num));
                }
            } else {
                if (isNum) {
                    nums.add(convert(num));
                    isNum = false;
                }
                num = new StringBuilder();
            }
            i++;
        }
        return nums.size();
    }

    private String convert(StringBuilder sb) {
        int i = 0;
        while (i < sb.length() && sb.charAt(i) == '0') {
            i++;
        }
        if (i < sb.length()) {
            return sb.substring(i);
        }
        return "0";
    }
}
