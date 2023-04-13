package com.leetcode;

/**
 * 917. Reverse Only Letters
 * https://leetcode.com/problems/reverse-only-letters/
 */
public class Problem917 {
    public String reverseOnlyLetters(String s) {
        char[] chars = s.toCharArray();
        int i = 0, j = s.length() - 1;
        while (i < j) {
            while (i < j && !Character.isAlphabetic(chars[i])) {
                i++;
            }
            while (i < j && !Character.isAlphabetic(chars[j])) {
                j--;
            }
            if (i < j) {
                char tmp = chars[i];
                chars[i] = chars[j];
                chars[j] = tmp;
                i++;
                j--;
            }
        }
        return String.valueOf(chars);
    }
}
