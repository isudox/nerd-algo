package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 847. Shortest Path Visiting All Nodes
 * https://leetcode.com/problems/shortest-path-visiting-all-nodes/
 */
public class Problem847 {
    private int[][] g;
    private boolean[] visited;
    private int ans = Integer.MAX_VALUE;

    public int shortestPathLength(int[][] graph) {
        this.g = graph;
        this.visited = new boolean[graph.length];
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < graph.length; i++) {
            queue.add(i);
        }
        while (queue.size() > 0) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                int pos = queue.pollFirst();
                for (int next : graph[pos]) {

                }
            }
        }
        return ans;
    }
}
