package com.leetcode;

/**
 * 48. Rotate Image
 * https://leetcode.com/problems/rotate-image/
 */
class Problem48 {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < (n + 1) / 2; i++) {
            rotate(matrix, i);
        }
    }

    private void rotate(int[][] matrix, int level) {
        int n = matrix.length;
        int d = n - level * 2;
        if (d < 2) {
            return;
        }
        for (int i = 0; i < d - 1; i++) { // rotate 4 nums for one loop
            int[] p1 = {level, level + i};
            int[] p2 = {level + i, n - level - 1};
            int[] p3 = {n - level - 1, n - level - 1 - i};
            int[] p4 = {n - level - 1 - i, level};
            swap(matrix, p1, p2, p3, p4);
        }
    }

    private void swap(int[][] matrix, int[] p1, int[] p2, int[] p3, int[] p4) {
        int t2 = matrix[p2[0]][p2[1]];
        matrix[p2[0]][p2[1]] = matrix[p1[0]][p1[1]];
        int t3 = matrix[p3[0]][p3[1]];
        matrix[p3[0]][p3[1]] = t2;
        int t4 = matrix[p4[0]][p4[1]];
        matrix[p4[0]][p4[1]] = t3;
        matrix[p1[0]][p1[1]] = t4;
    }
}
