package com.leetcode;

/**
 * 921. Minimum Add to Make Parentheses Valid
 * https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
 */
public class Problem921 {
    public int minAddToMakeValid(String s) {
        int left = 0, insert = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else if (left > 0) {
                left--;
            } else {
                insert++;
            }
        }
        return insert + left;
    }
}
