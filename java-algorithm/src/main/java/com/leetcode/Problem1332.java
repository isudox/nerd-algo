package com.leetcode;

/**
 * 1332. Remove Palindromic Subsequences
 * https://leetcode.com/problems/remove-palindromic-subsequences/
 */
public class Problem1332 {
    public int removePalindromeSub(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return 2;
            }
            i++;
            j--;
        }
        return 1;
    }
}
