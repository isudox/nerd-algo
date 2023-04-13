package com.leetcode;

/**
 * 583. Delete Operation for Two Strings
 * https://leetcode.com/problems/delete-operation-for-two-strings/
 */
public class Problem583 {
    public int minDistance(String word1, String word2) {
        int[][] memo = new int[word1.length() + 1][word2.length() + 1];
        return word1.length() + word2.length() - 2 * helper(word1, word2, word1.length(), word2.length(), memo);
    }

    private int helper(String a, String b, int m, int n, int[][] memo) {
        if (m == 0 || n == 0) {
            return 0;
        }
        if (memo[m][n] != 0) {
            return memo[m][n];
        }
        if (a.charAt(m - 1) == b.charAt(n - 1)) {
            memo[m][n] = helper(a, b, m - 1, n - 1, memo) + 1;
        } else {
            memo[m][n] = Math.max(helper(a, b, m, n - 1, memo), helper(a, b, m - 1, n, memo));
        }
        return memo[m][n];
    }
}
