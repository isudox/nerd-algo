package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 885. Spiral Matrix III
 * https://leetcode.com/problems/spiral-matrix-iii/
 */
public class Problem885 {
    public int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        List<int[]> path = new ArrayList<>();
        path.add(new int[]{rStart, cStart});
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // right, down, left, up
        int d = 0;
        int edge = 2;  // 当前方向边长
        int steps = 1; // 当前方向步数
        int r = rStart, c = cStart;
        while (path.size() < rows * cols) {
            r += dirs[d][0];
            c += dirs[d][1];
            if (0 <= r && r < rows && 0 <= c && c < cols) {
                path.add(new int[]{r, c});
            }
            steps++;
            if (steps == edge) {
                d = (d + 1) % 4;
                steps = 1; // 换方向后，重置步数
                if (d == 2 || d == 0) {
                    edge++;
                }
            }
        }
        int[][] ans = new int[rows * cols][2];
        for (int i = 0; i < rows * cols; i++) {
            ans[i] = path.get(i);
        }
        return ans;
    }
}
