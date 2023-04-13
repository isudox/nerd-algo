package com.leetcode;

import java.util.*;

/**
 * 1293. Shortest Path in a Grid with Obstacles Elimination
 * https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
 */
public class Problem1293 {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        if (m == 1 && n == 1) {
            return 0;
        }
        k = Math.min(k, m + n - 3);  // L 型路线最多使用 m+n-3
        Set<Tuple> visited = new HashSet<>();
        Deque<Tuple> q = new ArrayDeque<>();
        q.offer(new Tuple(0, 0, k));
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int steps = 0;
        while (!q.isEmpty()) {
            steps++;
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                Tuple t = q.pollFirst();
                for (int[] d : dirs) {
                    int nx = t.r + d[0], ny = t.c + d[1];
                    if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                        Tuple nt = new Tuple(nx, ny, t.k);
                        if (grid[nx][ny] == 0 && !visited.contains(nt)) {
                            if (nx == m - 1 && ny == n - 1) {
                                return steps;
                            }
                            q.offerLast(nt);
                            visited.add(nt);
                        } else if (grid[nx][ny] == 1 && t.k > 0) {
                            nt = new Tuple(nx, ny, t.k - 1);
                            if (!visited.contains(nt)) {
                                q.offerLast(nt);
                                visited.add(nt);
                            }
                        }
                    }
                }
            }
        }
        return -1;
    }

    private static class Tuple {
        public int r;
        public int c;
        public int k;

        public Tuple(int r, int c, int k) {
            this.r = r;
            this.c = c;
            this.k = k;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Tuple tuple = (Tuple) o;
            return r == tuple.r && c == tuple.c && k == tuple.k;
        }

        @Override
        public int hashCode() {
            return Objects.hash(r, c, k);
        }
    }
}
