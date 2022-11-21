package com.leetcode;

/**
 * 808. Soup Servings
 * https://leetcode.com/problems/soup-servings/
 */
public class Problem808 {
    public double soupServings(int n) {
        n = (int) Math.ceil((double) n / 25);
        if (n >= 179) {
            return 1;
        }
        double[][] memo = new double[n + 1][n + 1];
        return dfs(n, n, memo);
    }

    private double dfs(int x, int y, double[][] memo) {
        if (x <= 0 && y <= 0) {
            return 0.5;
        }
        if (x <= 0) {
            return 1;
        }
        if (y <= 0) {
            return 0;
        }
        if (memo[x][y] != 0) {
            return memo[x][y];
        }
        return memo[x][y] = 0.25 * (dfs(x - 4, y, memo) + dfs(x - 3, y - 1, memo) + dfs(x - 2, y - 2, memo) + dfs(x - 1, y - 3, memo));
    }
}
