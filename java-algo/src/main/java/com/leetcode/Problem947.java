package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 947. Most Stones Removed with Same Row or Column
 * https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
 */
public class Problem947 {
    public int removeStones(int[][] stones) {
        int n = stones.length;
        List<List<Integer>> edge = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            edge.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                if (i != j && stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    edge.get(i).add(j);
                }
            }
        }
        boolean[] visited = new boolean[n];
        int num = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                num++;
                dfs(i, edge, visited);
            }
        }
        return n - num;
    }

    public void dfs(int i, List<List<Integer>> edge, boolean[] visited) {
        visited[i] = true;
        for (int y : edge.get(i)) {
            if (!visited[y]) {
                dfs(y, edge, visited);
            }
        }
    }
}
