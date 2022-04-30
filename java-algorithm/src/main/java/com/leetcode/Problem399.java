package com.leetcode;

import java.util.*;

/**
 * 399. Evaluate Division
 * https://leetcode.com/problems/evaluate-division/
 */
public class Problem399 {
    private Map<String, Set<String>> graph = new HashMap<>();
    private Map<String, Double> edges = new HashMap<>();

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int n = values.length;
        for (int i = 0; i < n; i++) {
            List<String> eq = equations.get(i);
            edges.put(eq.get(0) + "->" + eq.get(1), values[i]);
            edges.put(eq.get(1) + "->" + eq.get(0), 1 / values[i]);
            Set<String> set = graph.getOrDefault(eq.get(0), new HashSet<>());
            set.add(eq.get(1));
            graph.put(eq.get(0), set);
            set = graph.getOrDefault(eq.get(1), new HashSet<>());
            set.add(eq.get(0));
            graph.put(eq.get(1), set);
        }
        double[] ans = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            List<String> query = queries.get(i);
            ans[i] = dfs(query.get(0), query.get(1), new HashSet<>());
        }
        return ans;
    }

    private double dfs(String start, String end, Set<String> visited) {
        if (!graph.containsKey(start) || !graph.containsKey(end)) {
            return -1.0;
        }
        if (Objects.equals(start, end)) {
            return 1.0;
        }
        String key1 = start + "->" + end, key2 = end + "->" + start;
        if (edges.containsKey(key1)) {
            return edges.get(key1);
        }
        if (edges.containsKey(key2)) {
            return edges.get(key2);
        }
        double ret = -1.0;
        visited.add(start);
        for (String next : graph.get(start)) {
            if (visited.contains(next)) {
                continue;
            }
            double tmp = dfs(next, end, visited);
            if (tmp != -1.0) {
                ret = tmp * edges.get(start + "->" + next);
                break;
            }
        }
        visited.remove(start);
        edges.put(key1, ret);
        edges.put(key2, 1 / ret);
        return ret;
    }
}
