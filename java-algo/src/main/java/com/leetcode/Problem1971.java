package com.leetcode;

import java.util.*;

/**
 * 1971. Find if Path Exists in Graph
 * https://leetcode.com/problems/find-if-path-exists-in-graph/
 */
public class Problem1971 {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination) {
            return true;
        }
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            Set<Integer> set0 = graph.getOrDefault(edge[0], new HashSet<>());
            set0.add(edge[1]);
            graph.put(edge[0], set0);
            Set<Integer> set1 = graph.getOrDefault(edge[1], new HashSet<>());
            set1.add(edge[0]);
            graph.put(edge[1], set1);
        }
        boolean[] visited = new boolean[n];
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(source);
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int cur = q.pollFirst();
                if (cur == destination) {
                    return true;
                }
                if (graph.containsKey(cur) && graph.get(cur).contains(destination)) {
                    return true;
                }
                for (int nxt : graph.get(cur)) {
                    if (visited[nxt]) {
                        continue;
                    }
                    visited[nxt] = true;
                    q.offerLast(nxt);
                }
            }
        }
        return false;
    }
}
