package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 54. Spiral Matrix
 * https://leetcode.com/problems/spiral-matrix/
 *
 * Given a matrix of m x n elements (m rows, n columns), return all elements of
 * the matrix in spiral order.
 *
 * Example 1:
 *
 * Input:
 * [
 *  [ 1, 2, 3 ],
 *  [ 4, 5, 6 ],
 *  [ 7, 8, 9 ]
 * ]
 * Output: [1,2,3,6,9,8,7,4,5]
 *
 * Example 2:
 *
 * Input:
 * [
 *   [1, 2, 3, 4],
 *   [5, 6, 7, 8],
 *   [9,10,11,12]
 * ]
 * Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 */
public class Problem54 {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (null == matrix) return new ArrayList<>();
        int rows = matrix.length;
        int cols = matrix[0].length;
        int size = rows * cols;
        List<Integer> ans = new ArrayList<>();
        int count = 0, row = 0, col = 0;
        int dir = 0;  // 0, 1, 2, 3: to right, downside, left, upside
        while (count < size) {
        }
        return ans;
    }

    private void move(int x, int y, int dir) {
        switch (dir) {
            case 0:

                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                break;
        }
    }
}
