package com.leetcode;

/**
 * 1641. Count Sorted Vowel Strings
 * https://leetcode.com/problems/count-sorted-vowel-strings/
 */
public class Problem1641 {
    private int[][] memo;

    public int countVowelStrings(int n) {
        memo = new int[5][n + 1];
        return dfs(0, n);
    }

    private int dfs(int start, int n) {
        if (n == 1) {
            return 5 - start;
        }
        if (memo[start][n] > 0) {
            return memo[start][n];
        }
        int ret = 0;
        for (int i = start; i < 5; i++) {
            ret += dfs(i, n - 1);
        }
        return memo[start][n] = ret;
    }
}
