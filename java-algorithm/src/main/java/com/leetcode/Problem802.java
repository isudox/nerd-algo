package com.leetcode;

import java.util.*;

/**
 * 802. Find Eventual Safe States
 * https://leetcode.com/problems/find-eventual-safe-statesd
 */
public class Problem802 {

    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        boolean[] visited = new boolean[n];
        boolean[] candidates = new boolean[n];
        Arrays.fill(candidates, true);
        Set<Integer> unsafe = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (!visited[i] && candidates[i]) {
                visited[i] = true;
                Set<Integer> path = new HashSet<>();
                path.add(i);
                dfs(i, path, graph, unsafe, visited);
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (candidates[i]) {
                ans.add(i);
            }
        }
        return ans;
    }

    private void dfs(int node, Set<Integer> path, int[][] graph, Set<Integer> unsafe, boolean[] visited) {
        for (int nextNode : graph[node]) {
            if (!unsafe.contains(nextNode) && !path.contains(nextNode)) {
                visited[nextNode] = true;
                path.add(nextNode);
                dfs(nextNode, path, graph, unsafe, visited);
                path.remove(nextNode);
            } else {
                unsafe.addAll(path);
            }
        }
    }
}
