package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1380. Lucky Numbers in a Matrix
 * https://leetcode.com/problems/lucky-numbers-in-a-matrix/
 */
public class Problem1380 {
    public List<Integer> luckyNumbers (int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int m = matrix.length, n = matrix[0].length;
        int[][] sorted = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sorted[i][j] = matrix[i][j];
            }
            Arrays.sort(sorted[i]);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == sorted[i][0]) {
                    boolean flag = true;
                    for (int k = 0; k < m; k++) {
                        if (matrix[k][j] > matrix[i][j]) {
                            flag = false;
                            break;
                        }
                    }
                    if (flag) {
                        ans.add(matrix[i][j]);
                    }
                }
            }
        }
        return ans;
    }
}
