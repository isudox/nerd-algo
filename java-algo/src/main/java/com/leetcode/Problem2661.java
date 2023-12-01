package com.leetcode;

/**
 * 2661. First Completely Painted Row or Column
 * https://leetcode.cn/problems/first-completely-painted-row-or-column/
 */
public class Problem2661 {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[][] xy = new int[arr.length + 1][2];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                xy[mat[i][j]][0] = i;
                xy[mat[i][j]][1] = j;
            }
        }
        int[] rowCnt = new int[m], colCnt = new int[n];
        for (int i = 0; i < arr.length; i++) {
            int x = xy[arr[i]][0], y = xy[arr[i]][1];
            if (++rowCnt[x] == n || ++colCnt[y] == m) {
                return i;
            }
        }
        return -1;
    }
}
