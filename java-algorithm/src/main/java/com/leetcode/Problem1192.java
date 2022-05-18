package com.leetcode;

import java.util.*;

/**
 * 1192. Critical Connections in a Network
 * https://leetcode.com/problems/critical-connections-in-a-network/
 */
public class Problem1192 {
    private Map<Integer, Set<Integer>> graph = new HashMap<>();

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        graph = new HashMap<>();
        for (List<Integer> conn : connections) {
            int u = conn.get(0), v = conn.get(1);
            Set<Integer> set = graph.getOrDefault(u, new HashSet<>());
            set.add(v);
            graph.put(u, set);
            set = graph.getOrDefault(v, new HashSet<>());
            set.add(u);
            graph.put(v, set);
        }

        int[] timestamps = new int[n];
        Arrays.fill(timestamps, -1);
        List<List<Integer>> ans = new ArrayList<>();
        dfs(0, -1, 0, timestamps, ans);
        return ans;
    }

    private int dfs(int cur, int pre, int ts, int[] timestamps, List<List<Integer>> store) {
        timestamps[cur] = ts;
        Set<Integer> set = graph.get(cur);
        for (Integer next : set) {
            if (next == pre) {
                continue;
            }
            if (timestamps[next] == -1) {
                timestamps[cur] = Math.min(timestamps[cur], dfs(next, cur, ts + 1, timestamps, store));
            } else {
                timestamps[cur] = Math.min(timestamps[cur], timestamps[next]);
            }
        }
        if (timestamps[cur] == ts && cur != 0) {
            store.add(Arrays.asList(pre, cur));
        }
        return timestamps[cur];
    }
}
