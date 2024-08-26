package com.leetcode;

import java.util.Arrays;

/**
 * 1460. Make Two Arrays Equal by Reversing Subarrays
 * https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
 */
public class Problem1460 {
    public boolean canBeEqual(int[] target, int[] arr) {
        Arrays.sort(target);
        Arrays.sort(arr);
        for (int i = 0; i < target.length; i++) {
            if (target[i] != arr[i]) {
                return false;
            }
        }
        return true;
    }
}
