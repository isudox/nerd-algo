package com.leetcode;

import java.util.TreeSet;

/**
 * 363. Max Sum of Rectangle No Larger Than K
 * https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
 *
 * Given an m x n matrix matrix and an integer k, return the max sum of a
 * rectangle in the matrix such that its sum is no larger than k.
 *
 * It is guaranteed that there will be a rectangle with a sum no larger than
 * k.
 *
 * Example 1:
 *
 * Input: matrix = [[1,0,1],[0,-2,3]], k = 2
 * Output: 2
 * Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
 * and 2 is the max number no larger than k (k = 2).
 *
 * Example 2:
 *
 * Input: matrix = [[2,2,-1]], k = 3
 * Output: 3
 *
 * Constraints:
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 100
 * -100 <= matrix[i][j] <= 100
 * -10^5 <= k <= 10^5
 *
 * Follow up: What if the number of rows is much larger than the number of
 * columns?
 */
public class Problem363 {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length, ans = Integer.MIN_VALUE;
        int[][] preSums = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                preSums[i][j] = preSums[i - 1][j] + preSums[i][j - 1] - preSums[i - 1][j - 1] + matrix[i - 1][j - 1];
                if (preSums[i][j] == k)
                    return k;
                if (preSums[i][j] < k && preSums[i][j] > ans)
                    ans = preSums[i][j];
            }
        }
        for (int x0 = 1; x0 <= m; x0++) {
            for (int y0 = 1; y0 <= n; y0++) {
                for (int x1 = x0; x1 <= m; x1++) {
                    for (int y1 = y0; y1 <= n; y1++) {
                        int cur = preSums[x1][y1] - preSums[x0 - 1][y1] - preSums[x1][y0 - 1] + preSums[x0 - 1][y0 - 1];
                        if (cur == k)
                            return k;
                        if (cur < k && cur > ans)
                            ans = cur;
                    }
                }
            }
        }
        return ans;
    }

    public int maxSumSubmatrix2(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < m; i++) {
            int[] colSums = new int[n];
            for (int j = i; j < m; j++) {
                for (int col = 0; col < n; col++) {
                    colSums[col] += matrix[j][col];
                }
                TreeSet<Integer> treeSet = new TreeSet<>();
                treeSet.add(0);
                int cur = 0;
                for (int colSum : colSums) {
                    cur += colSum;
                    Integer ceil = treeSet.ceiling(cur - k);
                    if (ceil != null) {
                        ans = Math.max(ans, cur - ceil);
                    }
                    treeSet.add(cur);
                }
            }
        }
        return ans;
    }

}
