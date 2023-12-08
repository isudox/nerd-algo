package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
 */
public class Problem1466 {
    public int minReorder(int n, int[][] connections) {
        List<int[]>[] g = new List[n];
        for (int i = 0; i < n; i++) {
            g[i] = new ArrayList<>();
        }
        for (int[] conn : connections) {
            g[conn[0]].add(new int[]{conn[1], 1});
            g[conn[1]].add(new int[]{conn[0], 0});
        }
        return dfs(0, -1, g);
    }

    public int dfs(int cur, int pre, List<int[]>[] g) {
        int ret = 0;
        for (int[] conn : g[cur]) {
            if (conn[0] == pre) {
                continue;
            }
            ret += conn[1] + dfs(conn[0], cur, g);
        }
        return ret;
    }
}
