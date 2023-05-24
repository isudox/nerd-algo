package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1377. Frog Position After T Seconds
 * https://leetcode.com/problems/frog-position-after-t-seconds/
 */
public class Problem1377 {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        boolean[] seen = new boolean[n + 1];
        return dfs(graph, seen, 1, t, target);
    }

    private double dfs(List<Integer>[] graph, boolean[] seen, int i, int t, int target) {
        int sz = graph[i].size() - (i == 1 ? 0 : 1);  // 非根结点的可选去向要去掉它的父节点
        if (t == 0 || sz == 0) {
            return i == target ? 1.0 : 0.0;
        }
        seen[i] = true;
        double ans = 0.0;
        for (int next : graph[i]) {
            if (!seen[next]) {
                ans += dfs(graph, seen, next, t - 1, target);
            }
        }
        return ans / sz;
    }
}
