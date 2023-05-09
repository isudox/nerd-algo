package com.leetcode;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

/**
 * 1263. Minimum Moves to Move a Box to Their Target Location
 * https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
 */
public class Problem1263 {
    public int minPushBox(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        int sx = -1, sy = -1, bx = -1, by = -1; // 玩家、箱子的初始位置
        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                if (grid[x][y] == 'S') {
                    sx = x;
                    sy = y;
                } else if (grid[x][y] == 'B') {
                    bx = x;
                    by = y;
                }
            }
        }
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int[][] dp = new int[m * n][m * n];
        for (int i = 0; i < m * n; i++) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        Queue<int[]> q = new ArrayDeque<>();
        dp[sx * n + sy][bx * n + by] = 0;
        q.offer(new int[]{sx * n + sy, bx * n + by});
        while (!q.isEmpty()) {
            Queue<int[]> q1 = new ArrayDeque<>();
            while (!q.isEmpty()) {
                int[] arr = q.poll();
                int s1 = arr[0], b1 = arr[1];
                int sx1 = s1 / n, sy1 = s1 % n, bx1 = b1 / n, by1 = b1 % n;
                if (grid[bx1][by1] == 'T') {
                    return dp[s1][b1];
                }
                for (int i = 0; i < 4; i++) {
                    int sx2 = sx1 + dirs[i][0], sy2 = sy1 + dirs[i][1], s2 = sx2 * n + sy2;
                    if (stop(grid, sx2, sy2)) {
                        continue;
                    }
                    if (bx1 == sx2 && by1 == sy2) {
                        int bx2 = bx1 + dirs[i][0], by2 = by1 + dirs[i][1], b2 = bx2 * n + by2;
                        if (stop(grid, bx2, by2) || dp[s2][b2] <= dp[s1][b1] + 1) {
                            continue;
                        }
                        dp[s2][b2] = dp[s1][b1] + 1;
                        q1.offer(new int[]{s2, b2});
                    } else {
                        if (dp[s2][b1] <= dp[s1][b1]) {
                            continue;
                        }
                        dp[s2][b1] = dp[s1][b1];
                        q.offer(new int[]{s2, b1});
                    }
                }
            }
            q = q1;
        }
        return -1;
    }

    public boolean stop(char[][] grid, int x, int y) {
        return x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] == '#';
    }
}
