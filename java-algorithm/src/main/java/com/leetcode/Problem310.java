package com.leetcode;

import java.util.*;

/**
 * 310. Minimum Height Trees
 * https://leetcode.com/problems/minimum-height-trees/
 */
public class Problem310 {

    private final Map<Integer, Set<Integer>> graph = new HashMap<>();
    private final Map<String, Integer> memo = new HashMap<>();
    private int n = 0;

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        this.n = n;
        for (int[] edge : edges) {
            int x = edge[0], y = edge[1];
            if (graph.containsKey(x)) {
                graph.get(x).add(y);
            } else {
                Set<Integer> set = new HashSet<>();
                set.add(y);
                graph.put(x, set);
            }
            if (graph.containsKey(y)) {
                graph.get(y).add(x);
            } else {
                Set<Integer> set = new HashSet<>();
                set.add(x);
                graph.put(y, set);
            }
        }
        List<Integer> roots = new ArrayList<>();
        int minHeight = n;
        for (int i = 0; i < n; i++) {
            int curHeight = 0;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    curHeight = Math.max(curHeight, dfs(i, j, new HashSet<>()));
                }
            }
            if (curHeight < minHeight) {
                minHeight = curHeight;
                roots.clear();
                roots.add(i);
            } else if (curHeight == minHeight) {
                roots.add(i);
            }
        }
        return roots;
    }

    private int dfs(int x, int y, Set<Integer> visited) {
        if (graph.get(x).contains(y)) {
            return 1;
        }
        String k1 = String.format("%d-%d", x, y), k2 = String.format("%d-%d", y, x);
        if (memo.containsKey(k1)) {
            return memo.get(k1);
        }
        if (memo.containsKey(k2)) {
            return memo.get(k2);
        }
        visited.add(x);
        int distance = this.n;
        for (int next : graph.get(x)) {
            if (!visited.contains(next)) {
                distance = Math.min(1 + dfs(next, y, visited), distance);
            }
        }
        visited.remove(x);
        if (distance < n) {
            memo.put(k1, distance);
        }
        return distance;
    }
}
