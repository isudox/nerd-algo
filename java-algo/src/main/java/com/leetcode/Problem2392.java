package com.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 2392. Build a Matrix With Conditions
 * https://leetcode.com/problems/build-a-matrix-with-conditions/
 * TODO
 */
public class Problem2392 {
    public int[][] buildMatrix(int k, int[][] rowConditions, int[][] colConditions) {
        int[][] ans = new int[k][k];
        List<Integer> sortRows = topoSort(rowConditions, k);
        List<Integer> sortCols = topoSort(colConditions, k);
        if (sortRows.isEmpty() || sortCols.isEmpty()) {
            return ans;
        }
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < k; j++) {
                if (sortRows.get(i).equals(sortCols.get(j))) {
                    ans[i][j] = sortRows.get(i);
                }
            }
        }
        return ans;
    }

    private List<Integer> topoSort(int[][] edges, int k) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= k; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
        }
        List<Integer> order = new ArrayList<>();
        int[] visited = new int[k + 1];
        boolean[] hasCycle = {false};
        for (int i = 1; i <= k; i++) {
            if (visited[i] == 0) {
                dfs(i, adj, visited, order, hasCycle);
                if (hasCycle[0]) {
                    return new ArrayList<>();
                }
            }
        }
        Collections.reverse(order);
        return order;
    }

    private void dfs(int node, List<List<Integer>> adj, int[] visited, List<Integer> order, boolean[] hasCycle) {
        visited[node] = 1;
        for (int nxt : adj.get(node)) {
            if (visited[nxt] == 0) {
                dfs(nxt, adj, visited, order, hasCycle);
                if (hasCycle[0]) {
                    return;
                }
            } else if (visited[nxt] == 1) {
                hasCycle[0] = true;
                return;
            }
        }
        visited[node] = 2;
        order.add(node);
    }
}
