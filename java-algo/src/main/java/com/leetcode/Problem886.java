package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 886. Possible Bipartition
 * https://leetcode.com/problems/possible-bipartition/
 */
public class Problem886 {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        List<Integer>[] graph = new List[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] dislike : dislikes) {
            graph[dislike[0]].add(dislike[1]);
            graph[dislike[1]].add(dislike[0]);
        }
        int[] groups = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            if (groups[i] == 0 && dfs(i, 1, groups, graph)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int node, int group, int[] groups, List<Integer>[] graph) {
        groups[node] = group;
        for (int next : graph[node]) {
            if (groups[next] == groups[node]) {
                return true;
            }
            if (groups[next] == 0 && dfs(next, 3 - group, groups, graph)) {
                return true;
            }
        }
        return false;
    }
}
