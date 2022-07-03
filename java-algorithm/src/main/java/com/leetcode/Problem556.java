package com.leetcode;

import java.util.Arrays;

/**
 * 556. Next Greater Element III
 * https://leetcode.com/problems/next-greater-element-iii/
 */
public class Problem556 {
    public int nextGreaterElement(int n) {
        boolean switched = false;
        String num = String.valueOf(n);
        char[] arr = num.toCharArray();
        int x = 0, y = arr.length - 1;
        int max = n % 10;
        for (int i = arr.length - 2; i >= 0; i--) {
            if (arr[i] - '0' < max) {
                switched = true;
                char closest = '9';
                for (int j = arr.length - 1; j > i; j--) {
                    if (arr[j] > arr[i] && arr[j] <= closest) {
                        closest = arr[j];
                        y = j;
                    }
                }
                x = i;
                break;
            } else {
                if (arr[i] - '0' > max) {
                    max = arr[i] - '0';
                }
            }
        }
        if (!switched) {
            return -1;
        }
        char tmp = arr[x];
        arr[x] = arr[y];
        arr[y] = tmp;
        char[] left = Arrays.copyOfRange(arr, 0, x + 1);
        char[] right = Arrays.copyOfRange(arr, x + 1, arr.length);
        Arrays.sort(right);
        long ans = 0L;
        for (char c : left) {
            ans = ans * 10 + (c - '0');
            if (ans > Integer.MAX_VALUE) {
                return -1;
            }
        }
        for (char c : right) {
            ans = ans * 10 + (c - '0');
            if (ans > Integer.MAX_VALUE) {
                return -1;
            }
        }
        return (int) ans;
    }
}
