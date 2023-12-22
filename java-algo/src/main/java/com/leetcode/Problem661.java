package com.leetcode;

public class Problem661 {
    public int[][] imageSmoother(int[][] img) {
        int m = img.length, n = img[0].length;
        int[][] ans = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans[i][j] = cal(img, i, j);
            }
        }
        return ans;
    }

    private int cal(int[][] grid, int x, int y) {
        int sum = 0, cnt = 0;
        int left = Math.max(0, y - 1);
        int right = Math.min(grid[0].length - 1, y + 1);
        int up = Math.max(0, x - 1);
        int down = Math.min(grid.length - 1, x + 1);
        for (int i = up; i <= down ; i++) {
            for (int j = left; j <= right; j++) {
                cnt++;
                sum += grid[i][j];
            }
        }
        return sum / cnt;
    }
}
