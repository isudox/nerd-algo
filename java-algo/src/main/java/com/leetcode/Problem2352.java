package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Problem2352 {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        Map<String, Integer> rowCount = new HashMap<>();
        Map<String, Integer> colCount = new HashMap<>();
        for (int[] row : grid) {
            StringBuilder sb = new StringBuilder();
            for (int num : row) {
                sb.append(num).append(",");
            }
            String key = sb.toString();
            rowCount.put(key, rowCount.getOrDefault(key, 0) + 1);
        }
        for (int c = 0; c < n; c++) {
            StringBuilder sb = new StringBuilder();
            for (int[] row : grid) {
                sb.append(row[c]).append(",");
            }
            String key = sb.toString();
            colCount.put(key, colCount.getOrDefault(key, 0) + 1);
        }
        int ans = 0;
        for (String key : rowCount.keySet()) {
            if (colCount.containsKey(key)) {
                ans += rowCount.get(key) * colCount.get(key);
            }
        }
        return ans;
    }
}
