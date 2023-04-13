package com.leetcode;

/**
 * <a href="https://leetcode.com/problems/count-different-palindromic-subsequences/">730. Count Different Palindromic Subsequences</a>
 */
public class Problem730 {
    public int countPalindromicSubsequences(String s) {
        int MOD = (int) 1e9 + 7;
        int n = s.length();
        int[][][] dp = new int[4][n][n];
        for (int i = 0; i < n; i++) {
            dp[s.charAt(i) - 'a'][i][i] = 1;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len - 1;
                for (char ch = 'a'; ch <= 'd'; ch++) {
                    int k = ch - 'a';
                    if (s.charAt(i) == ch && s.charAt(j) == ch) {
                        dp[k][i][j] = (2 + (dp[0][i + 1][j - 1] + dp[1][i + 1][j - 1]) % MOD + (dp[2][i + 1][j - 1] + dp[3][i + 1][j - 1]) % MOD) % MOD;
                    } else if (s.charAt(i) == ch) {
                        dp[k][i][j] = dp[k][i][j - 1];
                    } else if (s.charAt(j) == ch) {
                        dp[k][i][j] = dp[k][i + 1][j];
                    } else {
                        dp[k][i][j] = dp[k][i + 1][j - 1];
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < 4; i++) {
            ans = (ans + dp[i][0][n - 1]) % MOD;
        }
        return ans;
    }
}
