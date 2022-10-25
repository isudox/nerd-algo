package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

/**
 * 934. Shortest Bridge
 * https://leetcode.com/problems/shortest-bridge/
 */
class Problem934 {
    private static final int[][] DIRS = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int shortestBridge(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Outer:
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    render(grid, i, j);
                    break Outer;
                }
            }
        }
        int ans = m * n;
        Deque<int[]> queue = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == -1) {
                    int len = 0;
                    queue.clear();
                    queue.offerLast(new int[]{i, j});
                    visited.clear();
                    visited.add(n * i + j);
                    Outer:
                    while (!queue.isEmpty()) {
                        int sz = queue.size();
                        for (int k = 0; k < sz; k++) {
                            int[] loc = queue.pollFirst();
                            visited.add(n * loc[0] + loc[1]);
                            for (int[] d : DIRS) {
                                int x = loc[0] + d[0], y = loc[1] + d[1];
                                if (0 <= x && x < m && 0 <= y && y < n && grid[x][y] != -1 && !visited.contains(n * x + y)) {
                                    if (grid[x][y] == 1) {
                                        ans = Math.min(ans, len);
                                        queue.clear();
                                        break Outer;
                                    }
                                    queue.offerLast(new int[]{x, y});
                                    visited.add(n * x + y);
                                }
                            }
                        }
                        len++;
                    }
                }
            }
        }
        return ans;
    }

    private void render(int[][] grid, int x, int y) {
        grid[x][y] = -1;
        for (int[] d : DIRS) {
            int nx = x + d[0], ny = y + d[1];
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] == 1) {
                render(grid, nx, ny);
            }
        }
    }
}
