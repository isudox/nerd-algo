package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1260. Shift 2D Grid
 * https://leetcode.com/problems/shift-2d-grid/submissions/
 */
public class Problem1260 {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int size = m * n;
        k %= size;
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(0);
            }
            ans.add(row);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int[] pos = helper(n,n * i + j + k, size);
                ans.get(pos[0]).set(pos[1], grid[i][j]);
            }
        }
        return ans;
    }

    private int[] helper(int n, int pos, int size) {
        int cnt = pos % size;
        return new int[]{cnt / n, cnt % n};
    }
}
