package com.leetcode;

/**
 * 1147. Longest Chunked Palindrome Decomposition
 * https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
 */
public class Problem1147 {
    public int longestDecomposition(String text) {
        if (text.length() == 1) {
            return 1;
        }
        int ans = 0, i = 0, j = text.length() - 1;
        StringBuilder pref = new StringBuilder();
        StringBuilder suff = new StringBuilder();
        while (i < j) {
            pref.append(text.charAt(i++));
            suff.insert(0, text.charAt(j--));
            if (pref.toString().equals(suff.toString())) {
                ans += 2;
                pref = new StringBuilder();
                suff = new StringBuilder();
            }
        }
        return i == j || !pref.isEmpty() ? ans + 1 : ans;
    }
}
