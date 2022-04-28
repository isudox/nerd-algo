package com.leetcode;

import java.util.*;

/**
 * 417. Pacific Atlantic Water Flow
 * https://leetcode.com/problems/pacific-atlantic-water-flow/
 */
public class Problem417 {
    private final int[][] DIRS = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];  // flow to pacific
        boolean[][] atlantic = new boolean[m][n]; // flow to atlantic
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    dfs(heights, pacific, i, j);
                }
                if (i == m - 1 || j == n - 1) {
                    dfs(heights, atlantic, i, j);
                }
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    ans.add(Arrays.asList(i, j));
                }
            }
        }
        return ans;
    }

    private void dfs(int[][] heights, boolean[][] visited, int x, int y) {
        if (visited[x][y]) {
            return;
        }
        visited[x][y] = true;
        int m = heights.length, n = heights[0].length;
        for (int[] dir : DIRS) {
            int nx = x + dir[0], ny = y + dir[1];
            if (0 <= nx && nx < m && 0 <= ny && ny < n && heights[nx][ny] >= heights[x][y]) {
                dfs(heights, visited, nx, ny);
            }
        }
    }

    public List<List<Integer>> pacificAtlantic2(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];  // flow to pacific
        boolean[][] atlantic = new boolean[m][n]; // flow to atlantic
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    bfs(heights, pacific, i, j);
                }
                if (i == m - 1 || j == n - 1) {
                    bfs(heights, atlantic, i, j);
                }
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    ans.add(Arrays.asList(i, j));
                }
            }
        }
        return ans;
    }

    private void bfs(int[][] heights, boolean[][] visited, int x, int y) {
        if (visited[x][y]) {
            return;
        }
        visited[x][y] = true;
        int m = heights.length, n = heights[0].length;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        while (!q.isEmpty()) {
            int[] cell = q.poll();
            for (int[] dir : DIRS) {
                int nx = cell[0] + dir[0], ny = cell[1] + dir[1];
                if (0 <= nx && nx < m && 0 <= ny && ny < n && heights[nx][ny] >= heights[cell[0]][cell[1]] && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
    }
}
