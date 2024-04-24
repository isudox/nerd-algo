package com.leetcode;

import java.util.*;

/**
 * 310. Minimum Height Trees
 * https://leetcode.com/problems/minimum-height-trees/
 */
public class Problem310 {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> ans = new ArrayList<>();
        if (n == 1) {
            ans.add(0);
            return ans;
        }
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        int[] degrees = new int[n];
        for (int[] edge : edges) {
            degrees[edge[0]]++;
            degrees[edge[1]]++;
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (degrees[i] == 1) {
                queue.add(i);
            }
        }
        while (!queue.isEmpty()) {
            ans = new ArrayList<>();
            int sz = queue.size();
            for (int i = 0; i < sz; i++) {
                int cur = queue.poll();
                ans.add(cur);
                List<Integer> neighbors = adj.get(cur);
                for (Integer neighbor : neighbors) {
                    degrees[neighbor]--;
                    if (degrees[neighbor] == 1) {
                        queue.add(neighbor);
                    }
                }
            }
        }
        return ans;
    }
}
