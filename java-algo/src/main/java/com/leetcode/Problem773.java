package com.leetcode;

import java.util.*;

/**
 * 773. Sliding Puzzle
 * https://leetcode.com/problems/sliding-puzzle/
 */
public class Problem773 {
    private static final int[][] MOVES = new int[][]{{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};

    public int slidingPuzzle(int[][] board) {
        String first = getString(board), target = getString(new int[][]{{1, 2, 3}, {4, 5, 0}});
        if (first.equals(target))
            return 0;
        Set<String> q1 = new HashSet<>(), q2 = new HashSet<>(), visited1 = new HashSet<>(), visited2 = new HashSet<>();
        q1.add(first);
        q2.add(target);
        visited1.add(first);
        visited2.add(target);
        int ans = 0;
        while (!q1.isEmpty()) {
            Set<String> nextStrings = new HashSet<>();
            for (String cur : q1) {
                if (q2.contains(cur))
                    return ans;
                nextStrings.addAll(nextBoards(cur, visited1));
            }
            ans++;
            q1 = nextStrings;
            if (q1.size() > q2.size()) {
                swap(q1, q2);
                swap(visited1, visited2);
            }
        }
        return -1;
    }

    private Set<String> nextBoards(String board, Set<String> visited) {
        int pos0 = board.indexOf("0");
        Set<String> strings = new HashSet<>();
        for (int pos : MOVES[pos0]) {
            String next = newString(board, pos0, pos);
            if (!visited.contains(next)) {
                strings.add(next);
                visited.add(next);
            }
        }
        return strings;
    }

    private String newString(String board, int i, int j) {
        char[] charArray = board.toCharArray();
        char temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return new String(charArray);
    }

    private void swap(Object o1, Object o2) {
        Object tmp = o1;
        o1 = o2;
        o2 = tmp;
    }

    private String getString(int[][] board) {
        StringBuilder sb = new StringBuilder();
        for (int[] row : board)
            for (int e : row)
                sb.append(e);
        return sb.toString();
    }
}
