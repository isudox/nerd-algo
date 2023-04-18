package com.leetcode;

/**
 * 1768. Merge Strings Alternately
 * https://leetcode.com/problems/merge-strings-alternately/
 */
public class Problem1768 {
    public String mergeAlternately(String word1, String word2) {
        int n = Math.min(word1.length(), word2.length());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(word1.charAt(i)).append(word2.charAt(i));
        }
        return sb.append(word1.length() > n ? word1.substring(n) : word2.substring(n)).toString();
    }
}
