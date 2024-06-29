package com.leetcode;

import java.util.*;

/**
 * 2192. All Ancestors of a Node in a Directed Acyclic Graph
 * https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
 */
public class Problem2192 {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer>[] parents = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            parents[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            parents[edge[1]].add(edge[0]);
        }
        for (int i = 0; i < n; i++) {
            Set<Integer> pars = new HashSet<>();
            dfs(parents, i, pars);
            List<Integer> ancestors = new ArrayList<>(pars);
            ancestors.sort(Integer::compareTo);
            ans.add(ancestors);
        }
        return ans;
    }

    private void dfs(List<Integer>[] parents, int i, Set<Integer> visited) {
        if (parents[i].isEmpty()) {
            return;
        }
        for (Integer parent : parents[i]) {
            if (!visited.contains(parent)) {
                visited.add(parent);
                dfs(parents, parent, visited);
            }
        }
    }
}
