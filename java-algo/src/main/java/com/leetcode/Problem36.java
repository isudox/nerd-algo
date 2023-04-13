package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 36. Valid Sudoku
 * https://leetcode.com/problems/valid-sudoku/
 *
 * Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
 * validated according to the following rules:
 *
 *   1. Each row must contain the digits 1-9 without repetition.
 *   2. Each column must contain the digits 1-9 without repetition.
 *   3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
 *      without repetition.
 *
 * <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png">
 *
 * The Sudoku board could be partially filled, where empty cells are filled
 * with the character '.'.
 *
 * Example 1:
 *
 * Input:
 * [
 *   ["5","3",".",".","7",".",".",".","."],
 *   ["6",".",".","1","9","5",".",".","."],
 *   [".","9","8",".",".",".",".","6","."],
 *   ["8",".",".",".","6",".",".",".","3"],
 *   ["4",".",".","8",".","3",".",".","1"],
 *   ["7",".",".",".","2",".",".",".","6"],
 *   [".","6",".",".",".",".","2","8","."],
 *   [".",".",".","4","1","9",".",".","5"],
 *   [".",".",".",".","8",".",".","7","9"]
 * ]
 * Output: true
 *
 * Example 2:
 *
 * Input:
 * [
 *   ["8","3",".",".","7",".",".",".","."],
 *   ["6",".",".","1","9","5",".",".","."],
 *   [".","9","8",".",".",".",".","6","."],
 *   ["8",".",".",".","6",".",".",".","3"],
 *   ["4",".",".","8",".","3",".",".","1"],
 *   ["7",".",".",".","2",".",".",".","6"],
 *   [".","6",".",".",".",".","2","8","."],
 *   [".",".",".","4","1","9",".",".","5"],
 *   [".",".",".",".","8",".",".","7","9"]
 * ]
 * Output: false
 * Explanation: Same as Example 1, except with the 5 in the top left corner being
 *     modified to 8. Since there are two 8's in the top left 3x3 sub-box,
 *     it is invalid.
 *
 * Note:
 *
 *  A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 *  Only the filled cells need to be validated according to the mentioned rules.
 *  The given board contain only digits 1-9 and the character '.'.
 *  The given board size is always 9x9.
 */
public class Problem36 {

    public boolean isValidSudoku(char[][] board) {
        List<List<Character>> rows = initStore(9);
        List<List<Character>> cols = initStore(9);
        List<List<Character>> boxes = initStore(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;

                if (rows.get(i).contains(c)) return false;
                rows.get(i).add(c);

                if (cols.get(j).contains(c)) return false;
                cols.get(j).add(c);

                int boxIndex = i / 3 + (j / 3) * 3;
                if (boxes.get(boxIndex).contains(c)) return false;
                boxes.get(boxIndex).add(c);
            }
        }

        return true;
    }

    private List<List<Character>> initStore(int size) {
        List<List<Character>> store = new ArrayList<>(size);

        for (int i = 0; i < size; i++) {
            store.add(new ArrayList<>(size));
        }

        return store;
    }
}
