package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 52. N-Queens II
 * https://leetcode.com/problems/n-queens-ii/
 */
public class Problem52 {
    private int ans;

    public int totalNQueens(int n) {
        List<List<String>> ans = new ArrayList<>();
        backtrack(0, n, new ArrayList<>());
        return this.ans;
    }

    private void backtrack(int row, int n, List<Integer> cols) {
        if (row == n) {
            ans++;
        }
        for (int col = 0; col < n; col++) { // 尝试在第 row 行，第 col 列放置皇后
            boolean invalid = false;
            for (int i = 0; i < cols.size(); i++) {
                int dy = col - cols.get(i), dx = row - i;
                if (dy == 0 || Math.abs(dx) == Math.abs(dy)) {
                    invalid = true;// 如果和之前放置的皇后相冲突，则表明第 i 列不可以放置
                    break;
                }
            }
            if (invalid) {
                continue;
            }
            cols.add(col);
            backtrack(row + 1, n, cols);
            cols.remove(cols.size() - 1);
        }
    }
}
