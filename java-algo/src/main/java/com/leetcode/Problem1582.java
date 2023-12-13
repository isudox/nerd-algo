package com.leetcode;

/**
 * 1582. Special Positions in a Binary Matrix
 * https://leetcode.com/problems/special-positions-in-a-binary-matrix/
 */
public class Problem1582 {
    public int numSpecial(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] rowSum = new int[m];
        int[] colSum = new int[n];
        for (int i = 0; i < m; i++) {
            int row = 0;
            for (int j = 0; j < n; j++) {
                row += mat[i][j];
            }
            rowSum[i] = row;
        }
        for (int i = 0; i < n; i++) {
            int col = 0;
            for (int j = 0; j < m; j++) {
                col += mat[j][i];
            }
            colSum[i] = col;
        }
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 1 && rowSum[i] == 1 && colSum[j] == 1) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
