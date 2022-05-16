package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1091. Shortest Path in Binary Matrix
 * https://leetcode.com/problems/shortest-path-in-binary-matrix/
 */
public class Problem1091 {
    private final int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }
        if (n == 1) {
            return 1;
        }
        Deque<int[]> deque = new ArrayDeque<>();
        deque.addLast(new int[]{0, 0});
        boolean[][] visited = new boolean[n][n];
        visited[0][0] = true;
        int ans = 1;
        while (!deque.isEmpty()) {
            int size = deque.size();
            for (int i = 0; i < size; i++) {
                int[] pos = deque.pollFirst();
                int x = pos[0], y = pos[1];
                for (int[] d : dirs) {
                    int nx = x + d[0], ny = y + d[1];
                    if (0 <= nx && nx < n && 0 <= ny && ny < n && grid[nx][ny] == 0 && !visited[nx][ny]) {
                        if (nx == n - 1 && ny == n - 1) {
                            return ans + 1;
                        }
                        deque.addLast(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
            ans++;
        }
        return -1;
    }
}
