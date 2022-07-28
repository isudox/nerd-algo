package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 593. Valid Square
 * https://leetcode.com/problems/valid-square/
 */
public class Problem593 {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] points = new int[][]{p1, p2, p3, p4};
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < 3; i++) {
            for (int j = i + 1; j < 4; j++) {
                int d = dist(points[i], points[j]);
                count.put(d, count.getOrDefault(d, 0) + 1);
            }
        }
        boolean flag2 = false, flag4 = false;
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int d = entry.getKey(), c = entry.getValue();
            if (c != 2 && c != 4) return false;
            if (d == 0) return false;
            if (c == 2) flag2 = true;
            if (c == 4) flag4 = true;
        }
        return flag2 && flag4;
    }

    private int dist(int[] a, int[] b) {
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
    }
}
