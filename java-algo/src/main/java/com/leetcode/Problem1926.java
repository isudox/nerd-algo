package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1926. Nearest Exit from Entrance in Maze
 * https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
 */
public class Problem1926 {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length, n = maze[0].length;
        Deque<int[]> deque = new ArrayDeque<>();
        deque.offerLast(entrance);
        maze[entrance[0]][entrance[1]] = '-';
        int ans = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!deque.isEmpty()) {
            int sz = deque.size();
            for (int i = 0; i < sz; i++) {
                int[] pos = deque.pollFirst();
                int x = pos[0], y = pos[1];
                for (int[] d : dirs) {
                    int nx = x + d[0], ny = y + d[1];
                    if (0 <= nx && nx < m && 0 <= ny && ny < n && maze[nx][ny] == '.') {
                        if (nx == 0 || nx == m - 1 || ny == 0 || ny == n - 1) {
                            return ans + 1;
                        }
                        maze[nx][ny] = '-';
                        deque.offerLast(new int[]{nx, ny});
                    }
                }
            }
            ans++;
        }
        return -1;
    }
}
