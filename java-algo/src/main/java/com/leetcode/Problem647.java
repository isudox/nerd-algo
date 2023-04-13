package com.leetcode;

/**
 * 647. Palindromic Substrings
 * https://leetcode.com/problems/palindromic-substrings/
 */
public class Problem647 {
    public int countSubstrings(String s) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            ans += extend(s, i, i);
            ans += extend(s, i, i + 1);
        }
        return ans;
    }

    private int extend(String s, int start, int end) {
        int ret = 0;
        while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            ret++;
            start--;
            end++;
        }
        return ret;
    }
}
