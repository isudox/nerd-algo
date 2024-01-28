package com.leetcode;

/**
 * 1074. Number of Submatrices That Sum to Target
 * https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
 */
public class Problem1074 {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int ans = 0;
        int rows = matrix.length, cols = matrix[0].length;
        int[][] preSum = new int[rows + 1][cols + 1];
        for (int i = 1; i <= rows; i++) {
            for (int j = 1; j <= cols; j++) {
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] + matrix[i - 1][j - 1] - preSum[i - 1][j - 1];
                if (preSum[i][j] == target) {
                    ans++;
                }
            }
        }
        for (int x1 = 1; x1 <= rows; x1++) {
            for (int x2 = x1; x2 <= rows; x2++) {
                for (int y1 = 1; y1 <= cols; y1++) {
                    for (int y2 = y1; y2 <= cols; y2++) {
                        if (x1 == x2 && y1 == y2)
                            continue;
                        if (x1 == x2 || y1 == y2) {
                            if (preSum[x2][y2] - preSum[x1][y1] == target)
                                ans++;
                        } else {
                            if (preSum[x2][y2] - preSum[x1][y2] - preSum[x2][y1] + preSum[x1][y1] == target)
                                ans++;
                        }
                    }
                }
            }
        }
        return ans;
    }
}
