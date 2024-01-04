package com.leetcode;

public class Problem2397 {
    public int maximumRows(int[][] matrix, int numSelect) {
        int m = matrix.length, n = matrix[0].length, ans = 0;
        int limit = 1 << n;
        int[] rowOnes = new int[m];
        for (int i = 0; i < m; i++) {
            for (int num : matrix[i]) {
                if (num == 1) {
                    rowOnes[i]++;
                }
            }
        }
        int rowZero = 0;
        for (int cnt : rowOnes) {
            if (cnt == 0) {
                rowZero++;
            }
        }
        for (int i = 0; i < limit; i++) {
            if (Integer.bitCount(i) != numSelect) {
                continue;
            }
            int[] count = new int[m];
            int temp = 0;
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 1) {
                    for (int k = 0; k < m; k++) {
                        if (matrix[k][j] == 1) {
                            if (++count[k] == rowOnes[k]) {
                                temp++;
                            }
                        }
                    }
                }
            }
            ans = Math.max(ans, temp);
        }
        return ans + rowZero;
    }
}
