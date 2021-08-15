package com.leetcode;

/**
 * 576. Out of Boundary Paths
 * https://leetcode.com/problems/out-of-boundary-paths/
 */
public class Problem576 {

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][] memo = new int[m][n][maxMove + 1];
        return dfs(m, n, maxMove, startRow, startColumn, memo);
    }

    public int dfs(int m, int n, int maxMove, int row, int col, int[][][] memo) {
        int ans = 0;
        if (m - row > maxMove && row + 1 > maxMove && n - col > maxMove && col + 1 > maxMove)
            return 0;
        if (memo[row][col][maxMove] != 0)
            return memo[row][col][maxMove];
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] dir : dirs) {
            int nextRow = row + dir[0], nextCol = col + dir[1];
            if (nextRow == m || nextRow < 0 || nextCol == n || nextCol < 0) {
                ans++;
            } else {
                ans = (ans + dfs(m, n, maxMove - 1, nextRow, nextCol, memo)) % 1000000007;
            }
        }
        return memo[row][col][maxMove] = ans;
    }

    public int findPaths2(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][] dp = new int[maxMove + 1][m][n];
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int move = 1; move <= maxMove; move++) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    for (int[] dir : dirs) {
                        int ni = i + dir[0], nj = j + dir[1];
                        if (ni < 0 || ni == m || nj < 0 || nj == n) {
                            dp[move][i][j] += 1;
                        } else {
                            dp[move][i][j] += dp[move - 1][ni][nj];
                            dp[move][i][j] %= 1000000007;
                        }
                    }
                }
            }
        }
        return dp[maxMove][startRow][startColumn];
    }
}
