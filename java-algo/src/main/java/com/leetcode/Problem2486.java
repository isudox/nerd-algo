package com.leetcode;

/**
 * 2486. Append Characters to String to Make Subsequence
 * https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
 */
public class Problem2486 {
    public int appendCharacters(String s, String t) {
        int i = 0, j = 0, ans = 0;
        while (i < s.length() && j < t.length()) {
            while (i < s.length() && s.charAt(i) != t.charAt(j)) {
                i++;
            }
            if (i == s.length()) {
                break;
            }
            i++;
            j++;
        }
        return ans + t.length() - j;
    }
}
