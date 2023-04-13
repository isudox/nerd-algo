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
                int ret = helper(store[i], store[j]);
                if (ret > ans) {
                    ans = ret;
                }
            }
        }
        return ans;
    }

    private int helper(int[] a, int[] b) {
        int cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < 26; i++) {
            if (a[i] > 0 && b[i] > 0) {
                return 0;
            }
            if (a[i] > 0) {
                cnt1 += a[i];
            }
            if (b[i] > 0) {
                cnt2 += b[i];
            }
        }
        return cnt1 * cnt2;
    }
}
