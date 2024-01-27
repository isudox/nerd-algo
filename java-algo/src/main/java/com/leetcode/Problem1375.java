package com.leetcode;

/**
 * 1375. Number of Times Binary String Is Prefix-Aligned
 * https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/
 */
public class Problem1375 {
    int left = -1;
    int right = -1;

    public int numTimesAllBlue(int[] flips) {
        int ans = 0;
        int[] arr = new int[flips.length];
        for (int f : flips) {
            arr[f - 1] = 1;
            if (check(arr, f - 1)) {
                ans++;
            }
        }
        return ans;
    }

    private boolean check(int[] arr, int x) {
        if (left + 1 != x) {
            if (x > right) {
                right = x;
            }
            return false;
        }
        for (int i = x; i < arr.length; i++) {
            if (arr[i] != 1) {
                break;
            }
            left++;
        }
        if (left > right) {
            right = left;
        }
        return left == right;
    }
}
