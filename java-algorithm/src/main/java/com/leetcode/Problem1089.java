package com.leetcode;

/**
 * 1089. Duplicate Zeros
 * https://leetcode.com/problems/duplicate-zeros/
 */
public class Problem1089 {
    public void duplicateZeros(int[] arr) {
        int cnt0 = 0;
        for (int num : arr) {
            if (num == 0) {
                cnt0++;
            }
        }
        int n = arr.length;
        int m = arr.length + cnt0;
        for (int i = n - 1, j = m - 1; i < j; i--, j--) {
            if (arr[i] != 0) {
                if (j < n) {
                    arr[j] = arr[i];
                }
            } else {
                if (j < n) {
                    arr[j] = arr[i];
                }
                j--;
                if (j < n) {
                    arr[j] = arr[i];
                }
            }
        }
    }
}
