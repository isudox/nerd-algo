package com.leetcode;

/**
 * 861. Score After Flipping Matrix
 * https://leetcode.com/problems/score-after-flipping-matrix/
 */
public class Problem861 {
    public int matrixScore(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int ans = (1 << (n - 1)) * m;
        for (int i = 1; i < n; i++) {
            int cnt = 0;
            for (int[] row : grid) {
                if (row[i] == row[0]) {
                    cnt++;
                }
            }
            cnt = Math.max(cnt, m - cnt);
            int columnScore = (1 << (n - i - 1)) * cnt;
            ans += columnScore;
        }
        return ans;
    }
}
