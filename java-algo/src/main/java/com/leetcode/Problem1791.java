package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1791. Find Center of Star Graph
 * https://leetcode.com/problems/find-center-of-star-graph/
 */
public class Problem1791 {
    public int findCenter(int[][] edges) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            if (counter.containsKey(u)) {
                return u;
            }
            counter.put(u, 1);
            if (counter.containsKey(v)) {
                return v;
            }
            counter.put(v, 1);
        }
        return 0;
    }
}
