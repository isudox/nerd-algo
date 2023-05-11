package com.leetcode;

/**
 * 1016. Binary String With Substrings Representing 1 To N
 * https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
 */
public class Problem1016 {
    public boolean queryString(String s, int n) {
        for (int i = 1; i <= n; i++) {
            String bin = Integer.toString(i, 2);
            if (!s.contains(bin)) {
                return false;
            }
        }
        return true;
    }
}
