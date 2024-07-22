package com.leetcode;

/**
 * 1605. Find Valid Matrix Given Row and Column Sums
 * https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
 */
public class Problem1605 {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int m = rowSum.length, n = colSum.length;
        int[][] ans = new int[m][n];
        for (int i = 0, j = 0; i < m && j < n;) {
            int r = rowSum[i], c = colSum[j];
            if (r < c) {
                colSum[j] -= r;
                ans[i++][j] = r;
            } else {
                rowSum[i] -= c;
                ans[i][j++] = c;
            }
        }
        return ans;
    }
}
