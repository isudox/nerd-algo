package com.leetcode;

/**
 * 1750. Minimum Length of String After Deleting Similar Ends
 * https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
 */
public class Problem1750 {
    public int minimumLength(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                break;
            }
            char cur = s.charAt(i);
            while (i <= j && s.charAt(i) == cur) {
                i++;
            }
            while (i <= j && s.charAt(j) == cur) {
                j--;
            }
        }
        return j - i + 1;
    }
}
