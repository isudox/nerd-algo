package com.leetcode;

/**
 * 344. Reverse String
 * https://leetcode.com/problems/reverse-string/
 */
public class Problem344 {
    public void reverseString(char[] s) {
        int i = 0, j = s.length - 1;
        while (i < j) {
            char tmp = s[i];
            s[i++] = s[j];
            s[j--] = tmp;
        }
    }
}
