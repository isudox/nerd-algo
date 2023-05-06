package com.leetcode;

/**
 * 879. Profitable Schemes
 * https://leetcode.com/problems/profitable-schemes/
 */
public class Problem879 {
    private int base = (int) 1e9 + 7;

    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int m = group.length;
        long[][][] dp = new long[m + 1][n + 1][minProfit + 1];
        for (int i = 0; i <= n; i++) {
            dp[0][i][0] = 1;
        }
        for (int i = 1; i <= m; i++) {
            int a = group[i - 1], b = profit[i - 1];
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= minProfit; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];
                    if (j >= a) {
                        int u = Math.max(k - b, 0);
                        dp[i][j][k] += dp[i - 1][j - a][u];
                        if (dp[i][j][k] >= base) {
                            dp[i][j][k] -= base;
                        }
                    }
                }
            }
        }
        return (int) dp[m][n][minProfit];
    }
}
