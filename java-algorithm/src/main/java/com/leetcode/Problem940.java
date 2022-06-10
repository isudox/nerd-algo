package com.leetcode;

/**
 * <a href="https//leetcode.com/problems/distinct-subsequences-ii/">940. Distinct Subsequences II</a>
 */
public class Problem940 {
    public int distinctSubseqII(String s) {
        int mod = (int) (1e9 + 7);
        int[] endWith = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int tmp = 0;
            for (int x : endWith) {
                tmp = (tmp + x) % mod;
            }
            endWith[s.charAt(i) - 'a'] = tmp + 1;
        }
        int ans = 0;
        for (int x : endWith) {
            ans = (ans + x) % mod;
        }
        return ans;
    }
}
