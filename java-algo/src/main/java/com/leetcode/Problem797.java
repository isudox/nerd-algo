package com.leetcode;

import java.util.*;

/**
 * 797. All Paths From Source to Target
 * https://leetcode.com/problems/all-paths-from-source-to-target/
 */
public class Problem797 {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        path.add(0);
        dfs(path, graph, ans);
        return ans;
    }

    private void dfs(List<Integer> path, int[][] graph, List<List<Integer>> ans) {
        int cur = path.get(path.size() - 1);
        if (cur == graph.length - 1) {
            List<Integer> newPath = new ArrayList<>(path.size());
            newPath.addAll(path);
            ans.add(newPath);
        }
        for (int next : graph[cur]) {
            path.add(next);
            dfs(path, graph, ans);
            path.remove(path.size() - 1);
        }
    }
}
