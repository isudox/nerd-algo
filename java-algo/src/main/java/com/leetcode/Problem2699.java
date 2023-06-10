package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 2699. Modify Graph Edge Weights
 * https://leetcode.com/problems/modify-graph-edge-weights/
 * TODO
 */
public class Problem2699 {
    public int[][] modifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : edges) {
            List<Integer> list0 = graph.getOrDefault(edge[0], new ArrayList<>());
            list0.add(edge[1]);
            graph.put(edge[0], list0);
            List<Integer> list1 = graph.getOrDefault(edge[1], new ArrayList<>());
            list1.add(edge[0]);
            graph.put(edge[1], list1);
        }

        return null;
    }
}
