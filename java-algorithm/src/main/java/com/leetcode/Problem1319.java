package com.leetcode;

public class Problem1319 {
    int[] parent;
    int[] rank;

    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) {
            return -1;
        }
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
        int required = 0;
        for (int[] conn : connections) {
            if (find(conn[0]) != find(conn[1])) {
                union(conn[0], conn[1]);
                required++;
            }
        }
        return n - 1 - required;
    }

    private void union(int x, int y) {
        int fx = find(x), fy = find(y);
        if (rank[fx] < rank[fy]) {
            int tmp = fx;
            fx = fy;
            fy = tmp;
        }
        parent[fy] = fx;
        rank[fx] += rank[fy];
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
}
