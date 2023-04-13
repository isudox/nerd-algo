package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 990. Satisfiability of Equality Equations
 * https://leetcode.com/problems/satisfiability-of-equality-equations/
 */
class Problem990 {
    public boolean equationsPossible(String[] equations) {
        Map<String, Set<String>> graph = new HashMap<>();
        for (String eq : equations) {
            String a = eq.substring(0, 1), b = eq.substring(3, 4), flag = eq.substring(1, 3);
            if (flag.charAt(0) == '=') {
                Set<String> set1 = graph.getOrDefault(a, new HashSet<>());
                set1.add(b);
                graph.put(a, set1);
                Set<String> set2 = graph.getOrDefault(b, new HashSet<>());
                set2.add(a);
                graph.put(b, set2);
            }
        }
        for (String eq : equations) {
            String a = eq.substring(0, 1), b = eq.substring(3, 4), flag = eq.substring(1, 3);
            if (flag.charAt(0) == '!') {
                if (dfs(graph, a, b, new HashSet<>())) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean dfs(Map<String, Set<String>> graph, String from, String to, Set<String> visited) {
        if (from.equals(to)) {
            return true;
        }
        if (visited.contains(from) || graph.get(from) == null) {
            return false;
        }
        if (graph.get(from).contains(to)) {
            return true;
        }
        visited.add(from);
        for (String next : graph.get(from)) {
            if (visited.contains(next)) {
                continue;
            }
            if (dfs(graph, next, to, visited)) {
                return true;
            }
        }
        visited.remove(from);
        return false;
    }
}
