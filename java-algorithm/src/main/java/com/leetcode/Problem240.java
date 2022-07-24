package com.leetcode;

/**
 * 240. Search a 2D Matrix II
 * https://leetcode.com/problems/search-a-2d-matrix-ii/
 */
public class Problem240 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix[0].length;
        for (int[] row : matrix) {
            if (row[0] > target) return false;
            if (row[n - 1] < target) continue;
            int lo = 0, hi = n - 1;
            while (lo <= hi) {
                int mid = (lo + hi) >> 1;
                int num = row[mid];
                if (num == target) return true;
                if (num < target) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return false;
    }
}
