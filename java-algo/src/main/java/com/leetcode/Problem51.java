package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 51. N-Queens
 * https://leetcode.com/problems/n-queens/
 */
public class Problem51 {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList<>();
        backtrack(0, n, new ArrayList<>(), ans);
        return ans;
    }

    private void backtrack(int row, int n, List<Integer> cols, List<List<String>> ans) {
        if (row == n) {
            List<String> tmp = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < n; j++) {
                    sb.append(j == cols.get(i) ? "Q" : ".");
                }
                tmp.add(sb.toString());
            }
            ans.add(tmp);
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
            backtrack(row + 1, n, cols, ans);
            cols.remove(cols.size() - 1);
        }
    }
}
