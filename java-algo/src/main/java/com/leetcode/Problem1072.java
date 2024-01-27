package com.leetcode;

import java.util.*;

/**
 * 1072. Flip Columns For Maximum Number of Equal Rows
 * https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
 */
public class Problem1072 {
    public int maxEqualRowsAfterFlips(int[][] matrix) {
        Map<String, Integer> counter = new HashMap<>();
        for (int[] row : matrix) {
            String arr = toString(row);
            counter.put(arr, counter.getOrDefault(arr, 0) + 1);
        }
        int ans = 0;
        Set<String> visited = new HashSet<>();
        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            String key = entry.getKey();
            if (visited.contains(key)) {
                continue;
            }
            String rev = reverse(key);
            ans = Math.max(ans, counter.get(key) + counter.getOrDefault(rev, 0));
            visited.add(key);
            visited.add(rev);
        }
        return ans == 0 ? 1 : ans;
    }

    private String toString(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int num : arr) {
            sb.append(num);
        }
        return sb.toString();
    }

    private String reverse(String arr) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length(); i++) {
            sb.append(arr.charAt(i) == '0' ? '1' : '0');
        }
        return sb.toString();
    }
}
