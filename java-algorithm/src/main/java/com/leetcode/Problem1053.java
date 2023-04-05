package com.leetcode;

/**
 * 1053. Previous Permutation With One Swap
 * https://leetcode.com/problems/previous-permutation-with-one-swap/
 */
public class Problem1053 {
    public int[] prevPermOpt1(int[] arr) {
        int i = arr.length - 1;
        int min = 10;
        while (i >= 0) {
            if (arr[i] <= min) {
                min = arr[i--];
                continue;
            }
            int j = i + 1, max = arr[j];
            for (int k = i + 1; k < arr.length; k++) {
                if (arr[k] > max) {
                    max = arr[k];
                    j = k;
                }
            }
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            break;
        }
        return arr;
    }
}
