package com.leetcode;

/**
 * 2108. Find First Palindromic String in the Array
 * https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
 */
public class Problem2108 {
    public String firstPalindrome(String[] words) {
        for (String word : words) {
            int i = 0, j = word.length() - 1;
            while (i < j) {
                if (word.charAt(i) != word.charAt(j)) {
                    break;
                }
                i++;
                j--;
            }
            if (i >= j) {
                return word;
            }
        }
        return "";
    }
}
