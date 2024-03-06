package com.leetcode;

import java.util.Arrays;

/**
 * 977. Squares of a Sorted Array
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 */
public class Problem977 {

    public int[] sortedSquares(int[] A) {
        int size = A.length;

        for (int i = 0; i < size; i++) {
            A[i] = A[i] * A[i];
        }

        Arrays.sort(A);
        return A;
    }

    public int[] sortedSquares2(int[] A) {
        int size = A.length;
        int[] res = new int[size];
        boolean[] index = new boolean[size];

        for (int i = 0; i < size; i++) {
            A[i] = A[i] * A[i];
        }

        for (int i = 0; i < size; i++) {
            int min = Integer.MAX_VALUE;
            int mark = 0;
            for (int j = 0; j < size; j++) {
                if (index[j])
                    continue;
                if (A[j] < min) {
                    min = A[j];
                    mark = j;
                }
            }
            res[i] = min;
            index[mark] = true;
        }

        return res;
    }
}
