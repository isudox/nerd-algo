package com.leetcode;

import java.util.*;

/**
 * 743. Network Delay Time
 * https://leetcode.com/problems/network-delay-time/
 */
public class Problem743 {
    Map<Integer, List<int[]>> graph;

    public int networkDelayTime(int[][] times, int n, int k) {
        graph = new HashMap<>();
        for (int[] time : times) {
            if (!graph.containsKey(time[0])) {
                graph.put(time[0], new ArrayList<>());
            }
            List<int[]> list = graph.get(time[0]);
            list.add(new int[]{time[1], time[2]});
            graph.put(time[0], list);
        }
        for (Map.Entry<Integer, List<int[]>> entry : graph.entrySet()) {
            List<int[]> list = entry.getValue();
            list.sort((o1, o2) -> o1[1] - o2[1]);
        }
        int[] memo = new int[n + 1];
        Arrays.fill(memo, Integer.MAX_VALUE);
        dfs(k, 0, memo);
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (memo[i] == Integer.MAX_VALUE) {
                return -1;
            }
            if (memo[i] > ans) {
                ans = memo[i];
            }
        }
        return ans;
    }

    private void dfs(int node, int time, int[] memo) {
        if (time >= memo[node]) {
            return;
        }
        memo[node] = time;
        if (graph.containsKey(node)) {
            for (int[] e : graph.get(node)) {
                dfs(e[0], time + e[1], memo);
            }
        }
    }
}
