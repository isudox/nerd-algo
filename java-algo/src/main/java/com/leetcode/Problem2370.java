package com.leetcode;

/**
 * 2370. Longest Ideal Subsequence
 * https://leetcode.com/problems/longest-ideal-subsequence
 */
public class Problem2370 {
    public int longestIdealString(String s, int k) {
        int[] dp = new int[26];
        for (char c : s.toCharArray()) {
            c -= 'a';
            for (int i = Math.max(c - k, 0); i <= Math.min(c + k, 25); i++) {
                dp[c] = Math.max(dp[c], dp[i]);
            }
            dp[c]++;
        }
        int ans = dp[0];
        for (int x : dp) {
            ans = Math.max(ans, x);
        }
        return ans;
    }
}
