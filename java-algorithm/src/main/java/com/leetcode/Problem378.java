package com.leetcode;

import java.util.PriorityQueue;

/**
 * 378. Kth Smallest Element in a Sorted Matrix
 * https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
 *
 * Given a n x n matrix where each of the rows and columns are sorted
 * in ascending order, find the kth smallest element in the matrix.
 *
 * Note that it is the kth smallest element in the sorted order,
 * not the kth distinct element.
 *
 * Example:
 *
 * matrix = [
 *    [ 1,  5,  9],
 *    [10, 11, 13],
 *    [12, 13, 15]
 * ],
 * k = 8,
 *
 * return 13.
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ n2.
 */
public class Problem378 {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int lo = matrix[0][0];
        int hi = matrix[n - 1][n - 1];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int row = n - 1;
            int col = 0;
            int count = 0;
            while (row >= 0 && col < n) {
                if (matrix[row][col] <= mid) {
                    count += row + 1;
                    col += 1;
                } else {
                    row -= 1;
                }
            }
            if (count < k) {
                lo = mid + 1;
            } else if (count > k) {
                hi = mid;
            } else {
                hi = mid;
                lo = mid - 1;
            }
        }
        return lo;
    }
    public int kthSmallest2(int[][] matrix, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int[] row : matrix) {
            for (int num : row) {
                pq.add(-num);
                if (pq.size() > k) pq.poll();
            }
        }
        return -pq.peek();
    }
}
