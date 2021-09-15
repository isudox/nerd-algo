package com.leetcode;

/**
 * 978. Longest Turbulent Subarray
 * https://leetcode.com/problems/longest-turbulent-subarray/
 */
public class Problem978 {
    public int maxTurbulenceSize(int[] arr) {
        int ans = 1;
        int i = 0;
        while (i < arr.length && arr.length - i > ans) {
            int j = i + 1;
            while (j < arr.length && arr[j] == arr[j - 1])
                j++;
            if (j == arr.length)
                break;
            i = j - 1;
            j++;
            while (j < arr.length) {
                if (arr[j] == arr[j - 1] || arr[j] > arr[j - 1] == arr[j - 1] > arr[j - 2])
                    break;
                j++;
            }
            ans = Math.max(ans, j - i);
            i = j - 1;
        }
        return ans;
    }
}
