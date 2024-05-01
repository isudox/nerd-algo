package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1992. Find All Groups of Farmland
 * https://leetcode.com/problems/find-all-groups-of-farmland/
 */
class Problem1992 {
    int[][] dirs = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
    int row, col;

    public int[][] findFarmland(int[][] land) {
        boolean[][] visited = new boolean[land.length][land[0].length];
        List<int[]> ans = new ArrayList<>();
        for (int i = 0; i < land.length; i++) {
            for (int j = 0; j < land[0].length; j++) {
                if (land[i][j] == 1 && !visited[i][j]) {
                    row = 0;
                    col = 0;
                    dfs(land, visited, i, j);
                    int[] arr = new int[]{i, j, row, col};
                    ans.add(arr);
                }
            }
        }
        return ans.toArray(int[][]::new);
    }

    private boolean isWithinFarm(int x, int y, int N, int M) {
        return x >= 0 && x < N && y >= 0 && y < M;
    }

    private void dfs(int[][] land, boolean[][] visited, int x, int y) {
        visited[x][y] = true;
        row = Math.max(row, x);
        col = Math.max(col, y);

        for (int[] dir : dirs) {
            int nx = x + dir[0], ny = y + dir[1];
            if (isWithinFarm(nx, ny, land.length, land[0].length) && !visited[nx][ny] && land[nx][ny] == 1) {
                dfs(land, visited, nx, ny);
            }
        }
    }
}
