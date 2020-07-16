package com.leetcode;

/**
 * 785. Is Graph Bipartite?
 * https://leetcode.com/problems/is-graph-bipartite/
 */
public class Problem785 {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        // 0 means unmarked, 1 means marked A, -1 means marked B
        int[] marked = new int[n];
        for (int i = 0; i < n; i++) {
            if (marked[i] == 0) {
                marked[i] = 1;
                if (!dfs(i, graph, marked)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean dfs(int idx, int[][] graph, int[] marked) {
        for (int point : graph[idx]) {
            if (marked[point] != 0) {
                if (marked[point] == marked[idx]) {
                    return false;
                }
            } else {
                marked[point] = -marked[idx];
                if (!dfs(point, graph, marked)) {
                    return false;
                }
            }
        }
        return true;
    }
}
