package com.leetcode;

/**
 * 72. Edit Distance
 * https://leetcode.com/problems/edit-distance/
 *
 * Given two strings word1 and word2, return the minimum number of operations
 * required to convert word1 to word2.
 *
 * You have the following three operations permitted on a word:
 *
 * Insert a character
 * Delete a character
 * Replace a character
 *
 * Example 1:
 *
 * Input: word1 = "horse", word2 = "ros"
 * Output: 3
 * Explanation:
 * horse -> rorse (replace 'h' with 'r')
 * rorse -> rose (remove 'r')
 * rose -> ros (remove 'e')
 *
 * Example 2:
 *
 * Input: word1 = "intention", word2 = "execution"
 * Output: 5
 * Explanation:
 * intention -> inention (remove 't')
 * inention -> enention (replace 'i' with 'e')
 * enention -> exention (replace 'n' with 'x')
 * exention -> exection (replace 'n' with 'c')
 * exection -> execution (insert 'u')
 *
 * Constraints:
 *
 * 0 <= word1.length, word2.length <= 500
 * word1 and word2 consist of lowercase English letters.
 */
public class Problem72 {

    /**
     * Bruce Force with DFS
     */
    public int minDistance1(String word1, String word2) {
        return dfs(word1, 0, word2, 0);
    }

    private int dfs(String word1, int i, String word2, int j) {
        if (i == word1.length()) {
            return word2.length() - j;
        }
        if (j == word2.length()) {
            return word1.length() - i;
        }
        if (word1.charAt(i) == word2.charAt(j)) {
            return dfs(word1, i + 1, word2, j + 1);
        }
        return Math.min(dfs(word1, i + 1, word2, j + 1),
                Math.min(dfs(word1, i + 1, word2, j), dfs(word1, i, word2, j + 1))) + 1;
    }

    /**
     * DFS + Memo
     */
    public int minDistance2(String word1, String word2) {
        int[][] memo = new int[word1.length() + 1][word2.length() + 1];
        for (int i = 0; i <= word1.length(); i++) {
            for (int j = 0; j <= word2.length(); j++) {
                memo[i][j] = -1;
            }
        }
        return dfs(word1, 0, word2, 0, memo);
    }

    private int dfs(String w1, int i, String w2, int j, int[][] memo) {
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        if (i == w1.length()) {
            return memo[i][j] = w2.length() - j;
        }
        if (j == w2.length()) {
            return memo[i][j] = w1.length() - i;
        }
        if (w1.charAt(i) == w2.charAt(j)) {
            return memo[i][j] = dfs(w1, i + 1, w2, j + 1, memo);
        }
        return memo[i][j] = Math.min(dfs(w1, i + 1, w2, j + 1, memo),
                Math.min(dfs(w1, i + 1, w2, j, memo), dfs(w1, i, w2, j + 1, memo))) + 1;
    }

    /**
     * DP, from right to left.
     */
    public int minDistance3(String word1, String word2) {
        int[][] dp = new int[word1.length() + 1][word2.length() + 1];
        for (int i = 0; i <= word1.length(); i++) {
            dp[i][word2.length()] = word1.length() - i;
        }
        for (int j = 0; j <= word2.length(); j++) {
            dp[word1.length()][j] = word2.length() - j;
        }
        for (int i = word1.length() - 1; i >= 0; i--) {
            for (int j = word2.length() - 1; j >= 0; j--) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    dp[i][j] = dp[i + 1][j + 1];
                } else {
                    dp[i][j] = Math.min(dp[i + 1][j + 1], Math.min(dp[i][j + 1], dp[i + 1][j])) + 1;
                }
            }
        }
        return dp[0][0];
    }

    /**
     * DP, from left to right.
     */
    public int minDistance4(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        // dp[i][j] means minimum ops to convert word1[0:i] to word2[0:j]
        int[][] dp = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= len2; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
            }
        }
        return dp[len1][len2];
    }
}
