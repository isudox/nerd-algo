package com.leetcode;

/**
 * 498. Diagonal Traverse
 * https://leetcode.com/problems/diagonal-traverse/
 */
public class Problem498 {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] ans = new int[m * n];
        int r = 0, c = 0, idx = 0;
        boolean flag = true;
        while (idx < m * n) {
            if (flag) {
                while (r >= 0 && c < n) {
                    ans[idx++] = mat[r--][c++];
                }
                flag = false;
                r++;
                c--;
                if (c == n - 1) {
                    r++;
                } else {
                    c++;
                }
            } else {
                while (r < m && c >= 0) {
                    ans[idx++] = mat[r++][c--];
                }
                flag = true;
                r--;
                c++;
                if (r == m - 1) {
                    c++;
                } else {
                    r++;
                }
            }
        }
        return ans;
    }
}
