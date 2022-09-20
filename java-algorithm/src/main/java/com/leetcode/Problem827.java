package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 827. Making A Large Island
 * https://leetcode.com/problems/making-a-large-island/
 */
public class Problem827 {
    private int[] parent;
    private int[] size;

    public int largestIsland(int[][] grid) {
        int n = grid.length;
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        UnionFind uf = new UnionFind(n * n + 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) continue;
                for (int[] d : dirs) {
                    int x = i + d[0], y = j + d[1];
                    if (0 <= x && x < n && 0 <= y && y < n && grid[x][y] != 0) {
                        uf.union(i * n + j + 1, x * n + y + 1);
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    ans = Math.max(ans, uf.size[uf.find(i * n + j + 1)]);
                } else {
                    int cur = 1;
                    Set<Integer> seen = new HashSet<>();
                    for (int[] d : dirs) {
                        int x = i + d[0], y = j + d[1];
                        if (0 <= x && x < n && 0 <= y && y < n && grid[x][y] != 0) {
                            int root = uf.find(x * n + y + 1);
                            if (seen.contains(root)) continue;
                            seen.add(root);
                            cur += uf.size[root];
                        }
                    }
                    ans = Math.max(ans, cur);
                }
            }
        }
        return ans;
    }

    private void union(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py)
            return;
        if (size[px] > size[py]) {
            union(y, x);
        } else {
            size[py] += size[px];
            parent[px] = parent[py];
        }
    }

    private int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    private static class UnionFind {
        private final int[] parent;
        private final int[] size;

        public UnionFind(int size) {
            this.parent = new int[size];
            this.size = new int[size];
            for (int i = 1; i < size; i++) {
                this.parent[i] = i;
                this.size[i] = 1;
            }
        }

        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        public void union(int x, int y) {
            int px = find(x), py = find(y);
            if (px == py) return;
            if (size[px] < size[py]) {
                int tmp = px;
                px = py;
                py = tmp;
            }
            size[px] += size[py];
            parent[py] = px;
        }
    }
}
