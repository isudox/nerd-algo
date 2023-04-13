package com.leetcode;

/**
 * 1790. Check if One String Swap Can Make Strings Equal
 * https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
 */
public class Problem1790 {
    public boolean areAlmostEqual(String s1, String s2) {
        int x = -1, y = -1;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (x == -1) {
                    x = i;
                } else if (y == -1) {
                    y = i;
                } else {
                    return false;
                }
            }
        }
        if (x == -1) {
            return true;
        }
        if (y == -1) {
            return false;
        }
        return s1.charAt(y) == s2.charAt(x) && s1.charAt(x) == s2.charAt(y);
    }
}
