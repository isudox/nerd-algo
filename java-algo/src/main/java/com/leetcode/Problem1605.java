package com.leetcode;

public class Problem1605 {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int m = rowSum.length, n = colSum.length;
        int[][] ans = new int[m][n];
        int i = 0, j = 0;
        while (i < m && j < n) {
            int x = Math.min(rowSum[i], colSum[j]);
            ans[i][j] = x;
            rowSum[i] -= x;
            colSum[j] -= x;
            if (rowSum[i] == 0) {
                i++;
            }
            if (colSum[j] == 0) {
                j++;
            }
        }
        return ans;
    }
}
