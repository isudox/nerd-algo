package com.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 873. Length of Longest Fibonacci Subsequence
 * https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
 */
public class Problem873 {
    public int lenLongestFibSubseq(int[] arr) {
        int n = arr.length;
        if (n < 3) {
            return 0;
        }
        Map<Integer, Integer> positions = new HashMap<>();
        for (int i = 0; i < n; i++) {
            positions.put(arr[i], i);
        }
        int[][] memo = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], -1);
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                ans = Math.max(ans, dfs(arr, positions, i, j, memo));
            }
        }
        return ans > 2 ? ans : 0;
    }

    private int dfs(int[] arr, Map<Integer, Integer> positions, int i, int j, int[][] memo) {
        if (j >= arr.length) return 1;
        if (memo[i][j] > 0) return memo[i][j];
        int next = arr[i] + arr[j];
        if (!positions.containsKey(next)) return memo[i][j] = 2;
        int ret = dfs(arr, positions, j, positions.get(next), memo);
        return memo[i][j] = ret + 1;
    }
}
