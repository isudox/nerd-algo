package com.leetcode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * 909. Snakes and Ladders
 * https://leetcode.com/problems/snakes-and-ladders/
 */
public class Problem909 {
    public int snakesAndLadders(int[][] board) {
        int n = board.length, size = board.length * board.length;
        boolean[] visited = new boolean[size + 1];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{1, 0});
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            for (int i = 1; i <= 6; i++) {
                int next = p[0] + i;
                if (next > size)
                    break;
                int[] pos = getPos(next, n);
                if (board[pos[0]][pos[1]] != -1)
                    next = board[pos[0]][pos[1]];
                if (next == size)
                    return p[1] + 1;
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(new int[]{next, p[1] + 1});
                }
            }
        }
        return -1;
    }

    private int[] getPos(int id, int n) {
        int r = (id - 1) / n, c = (id - 1) % n;
        if (r % 2 == 1) {
            c = n - 1 - c;
        }
        return new int[]{n - 1 - r, c};
    }
}
