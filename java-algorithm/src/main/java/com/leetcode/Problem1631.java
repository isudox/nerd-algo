package com.leetcode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 1631. Path With Minimum Effort
 * https://leetcode.com/problems/path-with-minimum-effort/
 */
public class Problem1631 {
    private static final int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int minimumEffortPath(int[][] heights) {
        int m = heights.length, n = heights[0].length;

        int ans = 0;
        int lo = 0, hi = 999999, mid; // binary search
        while (lo <= hi) {
            mid = (lo + hi) / 2;
            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{0, 0});
            boolean[][] seen = new boolean[m][n];
            seen[0][0] = true;
            while (!queue.isEmpty()) {
                int[] cell = queue.poll();
                int x = cell[0], y = cell[1];
                for (int[] dir : dirs) {
                    int nx = x + dir[0], ny = y + dir[1];
                    if (0 <= nx && nx < m && 0 <= ny && ny < n && !seen[nx][ny] && Math.abs(heights[x][y] - heights[nx][ny]) <= mid) {
                        queue.offer(new int[]{nx, ny});
                        seen[nx][ny] = true;
                    }
                }
            }
            if (seen[m - 1][n - 1]) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
