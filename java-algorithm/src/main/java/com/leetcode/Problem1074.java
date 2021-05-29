package com.leetcode;

/**
 * 1074. Number of Submatrices That Sum to Target
 * https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
 *
 * Given a matrix and a target, return the number of non-empty submatrices that
 * sum to target.
 *
 * A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x
 * <= x2 and y1 <= y <= y2.
 *
 * Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
 * they have some coordinate that is different: for example, if x1 != x1'.
 *
 * Example 1:
 *
 * Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
 * Output: 4
 * Explanation: The four 1x1 submatrices that only contain 0.
 *
 * Example 2:
 *
 * Input: matrix = [[1,-1],[-1,1]], target = 0
 * Output: 5
 * Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the
 * 2x2 submatrix.
 *
 * Example 3:
 *
 * Input: matrix = [[904]], target = 0
 * Output: 0
 *
 * Constraints:
 *
 * 1 <= matrix.length <= 100
 * 1 <= matrix[0].length <= 100
 * -1000 <= matrix[i] <= 1000
 * -10^8 <= target <= 10^8
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
