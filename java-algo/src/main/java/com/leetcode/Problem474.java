package com.leetcode;

import java.util.Arrays;

/**
 * 474. Ones and Zeroes
 * https://leetcode.com/problems/ones-and-zeroes/
 */
public class Problem474 {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][][] dp = new int[strs.length + 1][m + 1][n + 1];
        for (int i = 1; i <= strs.length; i++) {
            int[] cnt = count(strs[i - 1]);
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];
                    if (j >= cnt[0] && k >= cnt[1]) {
                        dp[i][j][k] = Math.max(dp[i][j][k], dp[i - 1][j - cnt[0]][k - cnt[1]] + 1);
                    }
                }
            }
        }
        return dp[strs.length][m][n];
    }

    public int findMaxForm2(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (String str : strs) {
            int[] cnt = count(str);
            for (int i = m; i >= cnt[0]; i--) {
                for (int j = n; j >= cnt[1]; j--) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - cnt[0]][j - cnt[1]] + 1);
                }
            }
        }
        return dp[m][n];
    }

    public int findMaxForm3(String[] strs, int m, int n) {
        int[][] counts = new int[strs.length][2];
        for (int i = 0; i < strs.length; i++) {
            counts[i] = count(strs[i]);
        }
        int[][][] memo = new int[strs.length][m + 1][n + 1];
        for (int[][] matrix : memo) {
            for (int[] row : matrix) {
                Arrays.fill(row, -1);
            }
        }
        return dfs(counts, 0, m, n, memo);
    }

    private int dfs(int[][] counts, int pos, int zeros, int ones, int[][][] memo) {
        if (pos == memo.length)
            return 0;
        if (memo[pos][zeros][ones] != -1)
            return memo[pos][zeros][ones];
        int ret = dfs(counts, pos + 1, zeros, ones, memo);
        if (zeros >= counts[pos][0] && ones >= counts[pos][1]) {
            ret = Math.max(ret, 1 + dfs(counts, pos + 1, zeros - counts[pos][0], ones - counts[pos][1], memo));
        }
        memo[pos][zeros][ones] = ret;
        return ret;
    }

    public int findMaxForm4(String[] strs, int m, int n) {
        int[][] counts = new int[strs.length][2];
        for (int i = 0; i < strs.length; i++) {
            counts[i] = count(strs[i]);
        }
        Arrays.sort(counts, (a, b) -> a[0] - b[0]);
        int[][][] memo = new int[strs.length][m + 1][n + 1];
        for (int[][] matrix : memo) {
            for (int[] row : matrix) {
                Arrays.fill(row, -1);
            }
        }
        return dfs2(counts, 0, m, n, memo);
    }

    private int dfs2(int[][] counts, int pos, int zeros, int ones, int[][][] memo) {
        if (pos == memo.length || zeros < counts[pos][0])
            return 0;
        if (memo[pos][zeros][ones] != -1)
            return memo[pos][zeros][ones];
        // if not pick current str.
        memo[pos][zeros][ones] = dfs2(counts, pos + 1, zeros, ones, memo);
        if (ones < counts[pos][1])
            return memo[pos][zeros][ones];
        return memo[pos][zeros][ones] = Math.max(memo[pos][zeros][ones],
                1 + dfs2(counts, pos + 1, zeros - counts[pos][0], ones - counts[pos][1], memo));
    }

    private int[] count(String str) {
        int[] cnt = new int[]{0, 0};
        for (char c : str.toCharArray()) {
            cnt[c - '0']++;
        }
        return cnt;
    }
}
