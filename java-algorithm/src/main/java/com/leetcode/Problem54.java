package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 54. Spiral Matrix
 * https://leetcode.com/problems/spiral-matrix/
 */
public class Problem54 {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (null == matrix)
            return new ArrayList<>();
        int m = matrix.length, n = matrix[0].length;
        boolean[][] visited = new boolean[m][n];
        int size = m * n;
        int x = 0, y = 0;
        int i = 0;  // 0, 1, 2, 3: to right, downside, left, upside
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        List<Integer> ans = new ArrayList<>();
        ans.add(matrix[0][0]);
        visited[0][0] = true;
        int cnt = 1;
        while (cnt < size) {
            int nx = x + dirs[i][0], ny = y + dirs[i][1];
            if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny]) {
                x = nx;
                y = ny;
            } else {
                i = (i + 1) % 4;
                x += dirs[i][0];
                y += dirs[i][1];
            }
            ans.add(matrix[x][y]);
            visited[x][y] = true;
            cnt++;
        }
        return ans;
    }
}
