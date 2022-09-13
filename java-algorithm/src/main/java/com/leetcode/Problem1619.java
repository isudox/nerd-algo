package com.leetcode;

import java.util.Arrays;

/**
 * 1619. Mean of Array After Removing Some Elements
 * https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
 */
public class Problem1619 {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        int deletedCnt = arr.length / 20;
        double sum = 0;
        for (int i = deletedCnt; i < arr.length - deletedCnt; i++) {
            sum += arr[i];
        }
        return sum / (arr.length - deletedCnt * 2);
    }
}
