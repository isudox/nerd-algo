package com.leetcode;

/**
 * 318. Maximum Product of Word Lengths
 * https://leetcode.com/problems/maximum-product-of-word-lengths/
 */
public class Problem318 {
    public int maxProduct(String[] words) {
        int ans = 0;
        int[][] store = new int[words.length][26];
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                store[i][words[i].charAt(j) - 'a'] += 1;
            }
        }
        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (helper(store[i], store[j])) {
                    ans = Math.max(ans, words[i].length() * words[j].length());
                }
            }
        }
        return ans;
    }

    private boolean helper(int[] a, int[] b) {
        for (int i = 0; i < 26; ++i) {
            if (a[i] > 0 && b[i] > 0) {
                return false;
            }
        }
        return true;
    }
}
