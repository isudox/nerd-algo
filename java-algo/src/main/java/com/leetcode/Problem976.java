package com.leetcode;

import java.util.Arrays;

/**
 * 976. Largest Perimeter Triangle
 * https://leetcode.com/problems/largest-perimeter-triangle/
 *
 * Given an array A of positive lengths, return the largest perimeter of
 * a triangle with non-zero area, formed from 3 of these lengths.
 *
 * If it is impossible to form any triangle of non-zero area, return 0.
 *
 * Example 1:
 *
 * Input: [2,1,2]
 * Output: 5
 *
 * Example 2:
 *
 * Input: [1,2,1]
 * Output: 0
 *
 * Example 3:
 *
 * Input: [3,2,3,4]
 * Output: 10
 *
 * Example 4:
 *
 * Input: [3,6,2,3]
 * Output: 8
 *
 * Note:
 *
 * 3 <= A.length <= 10000
 * 1 <= A[i] <= 10^6
 */
public class Problem976 {
    public int largestPerimeter(int[] A) {
        Arrays.sort(A);
        int i = A.length - 1;
        while (i > 1) {
            if (A[i] < A[i - 1] + A[i - 2])
                return A[i] + A[i - 1] + A[i - 2];
            i--;
        }
        return 0;
    }
}
