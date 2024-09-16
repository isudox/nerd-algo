package com.leetcode;

/**
 * 1310. XOR Queries of a Subarray
 * https://leetcode.com/problems/xor-queries-of-a-subarray/
 */
public class Problem1310 {
    public int[] xorQueries(int[] arr, int[][] queries) {
        for (int i = 1; i < arr.length; i++) {
            arr[i] ^= arr[i - 1];
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int left = queries[i][0], right = queries[i][1];
            ans[i] = arr[right] ^ (left == 0 ? 0 : arr[left - 1]);
        }
        return ans;
    }
}
