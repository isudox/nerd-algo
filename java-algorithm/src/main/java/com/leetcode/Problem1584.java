package com.leetcode;

import java.util.*;

/**
 * 1584. Min Cost to Connect All Points
 * https://leetcode.com/problems/min-cost-to-connect-all-points/
 */
public class Problem1584 {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        if (n < 2) {
            return 0;
        }
        UnionFind uf = new UnionFind(n);
        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                edges.add(new Edge(cal(points[i], points[j]), i, j));
            }
        }
        edges.sort(Comparator.comparingInt(o -> o.len));
        int ans = 0, cnt = 1;
        for (Edge edge : edges) {
            int len = edge.len, x = edge.x, y = edge.y;
            if (uf.union(x, y)) {
                ans += len;
                cnt++;
                if (cnt == n) {
                    break;
                }
            }
        }
        return ans;
    }

    private int cal(int[] x, int[] y) {
        return Math.abs(x[0] - y[0]) + Math.abs(x[1] - y[1]);
    }

    private static class UnionFind {
        int[] f;
        int[] rank;
        int n;

        public UnionFind(int n) {
            this.n = n;
            this.rank = new int[n];
            Arrays.fill(this.rank, 1);
            this.f = new int[n];
            for (int i = 0; i < n; i++) {
                this.f[i] = i;
            }
        }

        public int find(int x) {
            return f[x] == x ? x : (f[x] = find(f[x]));
        }

        public boolean union(int x, int y) {
            int fx = find(x), fy = find(y);
            if (fx == fy) {
                return false;
            }
            if (rank[fx] < rank[fy]) {
                int tmp = fx;
                fx = fy;
                fy = tmp;
            }
            rank[fx] += rank[fy];
            f[fy] = fx;
            return true;
        }
    }

    private static class Edge {
        int len;
        int x;
        int y;

        public Edge(int len, int x, int y) {
            this.len = len;
            this.x = x;
            this.y = y;
        }
    }
}
