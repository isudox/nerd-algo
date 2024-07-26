package com.leetcode;

import java.util.*;

/**
 * 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
 * https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
 */
public class Problem1334 {
    Map<Integer, Set<Integer>> graph = new HashMap<>();
    Set<Integer> visited = new HashSet<>();
    Map<Integer, Integer> nearest = new HashMap<>();
    int threshold = 0;

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        threshold = distanceThreshold;
        int[][] weights = new int[n][n];
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            weights[u][v] = w;
            weights[v][u] = w;
            Set<Integer> set0 = graph.getOrDefault(u, new HashSet<>());
            set0.add(v);
            graph.put(u, set0);
            Set<Integer> set1 = graph.getOrDefault(v, new HashSet<>());
            set1.add(u);
            graph.put(v, set1);
        }
        int ans = -1, smallest = n;
        for (int i = 0; i < n; i++) {
            dfs(weights, i, i, 0);
            if (visited.size() <= smallest) {
                ans = i;
                smallest = visited.size();
            }
            visited.clear();
            nearest.clear();
        }
        return ans;
    }

    private void dfs(int[][] weights, int start, int cur, int dist) {
        if (!graph.containsKey(cur) || dist >= threshold) {
            return;
        }
        for (int next : graph.get(cur)) {
            int w = weights[cur][next];
            if (visited.contains(next) && nearest.get(next) <= dist + w) {
                continue;
            }
            if (dist + w <= threshold && next != start) {
                visited.add(next);
                nearest.put(next, dist + w);
                dfs(weights, start, next, dist + w);
            }
        }
    }
}
