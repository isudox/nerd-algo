package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 212. Word Search II
 * https://leetcode.com/problems/word-search-ii/
 */
public class Problem212 {
    private final Map<Character, List<int[]>> pos = new HashMap<>();
    private final int[][] dirs = new int[][]{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    public List<String> findWords(char[][] board, String[] words) {
        List<String> ans = new ArrayList<>();
        if (board.length == 0 || board[0].length == 0) return ans;
        int rows = board.length, cols = board[0].length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pos.containsKey(board[i][j])) {
                    pos.get(board[i][j]).add(new int[]{i, j});
                } else {
                    List<int[]> newPos = new ArrayList<>();
                    newPos.add(new int[]{i, j});
                    pos.put(board[i][j], newPos);
                }
            }
        }
        for (String word : words) {
            if (validate(board, word)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean validate(char[][] board, String word) {
        if (!pos.containsKey(word.charAt(0))) return false;
        List<int[]> positions = pos.get(word.charAt(0));
        for (int[] p : positions) {
            boolean[][] memo = new boolean[board.length][board[0].length];
            if (dfs(board, word, 1, p[0], p[1], memo))
                return true;
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int next, int row, int col, boolean[][] memo) {
        if (next == word.length()) return true;
        memo[row][col] = true;
        for (int[] d : dirs) {
            int x = row + d[0], y = col + d[1];
            if (x >= 0 && x < board.length && y >= 0 && y < board[0].length && !memo[x][y]) {
                if (board[x][y] == word.charAt(next)) {
                    memo[x][y] = true;
                    if (!dfs(board, word, next + 1, x, y, memo))
                        memo[x][y] = false;
                    else
                        return true;
                }
            }
        }
        return false;
    }
}
