package com.leetcode;

public class Problem1620 {
    public int[] bestCoordinate(int[][] towers, int radius) {
        int[][] g = new int[110][110];
        int m = 0, n = 0, val = 0;
        for (int[] tower : towers) {
            int x = tower[0], y = tower[1], q = tower[2];
            for (int i = Math.max(0, x - radius); i <= x + radius; i++) {
                for (int j = Math.max(0, y - radius); j <= y + radius; j++) {
                    double d = Math.sqrt((x - i) * (x - i) + (y - j) * (y - j));
                    if (d > radius) {
                        continue;
                    }
                    g[i][j] += Math.floor(q / (1 + d));
                    if (g[i][j] > val) {
                        m = i;
                        n = j;
                        val = g[i][j];
                    } else if (g[i][j] == val && (i < m || (i == m && j < n))) {
                        m = i;
                        n = j;
                    }
                }
            }
        }
        return new int[]{m, n};
    }
}
