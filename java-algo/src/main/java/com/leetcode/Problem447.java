package com.leetcode;

import java.util.*;

/**
 * https://leetcode.com/problems/number-of-boomerangs/
 */
public class Problem447 {
    public int numberOfBoomerangs(int[][] points) {
        int ans = 0;
        int n = points.length;
        for (int i = 0; i < n; i++) {
            Map<Integer, Integer> counts = new HashMap<>();
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }
                int x = points[i][0] - points[j][0];
                int y = points[i][1] - points[j][1];
                int d = x * x + y * y;
                counts.put(d, counts.getOrDefault(d, 0) + 1);
            }
            for (int cnt : counts.values()) {
                ans += cnt * (cnt - 1);
            }
        }
        return ans;
    }
}
