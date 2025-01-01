package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;

/**
 * 962. Maximum Width Ramp
 * https://leetcode.com/problems/maximum-width-ramp/
 */
public class Problem962 {
    public int maxWidthRamp(int[] arr) {
        int n = arr.length, ans = 0;
        Integer[] index = new Integer[n];
        for (int i = 0; i < n; i++) {
            index[i] = i;
        }
        Arrays.sort(index, Comparator.comparingInt(i -> arr[i]));
        int minPos = n;
        for (int i : index) {
            ans = Math.max(ans, i - minPos);
            minPos = Math.min(minPos, i);
        }
        return ans;
    }
}
