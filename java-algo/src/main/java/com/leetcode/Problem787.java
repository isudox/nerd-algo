package com.leetcode;

import java.util.*;

/**
 * 787. Cheapest Flights Within K Stops
 * https://leetcode.com/problems/cheapest-flights-within-k-stops/
 */
public class Problem787 {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[][] edges = new int[n][n];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] f : flights) {
            edges[f[0]][f[1]] = f[2];
            List<Integer> list = graph.getOrDefault(f[0], new ArrayList<>());
            list.add(f[1]);
            graph.put(f[0], list);
        }
        int ans = Integer.MAX_VALUE;
        int[] minPrices = new int[n];
        Arrays.fill(minPrices, Integer.MAX_VALUE);
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{src, 0});  // stop, total price
        while (!q.isEmpty() && k >= 0) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                int[] tuple = q.pollFirst();
                int stop = tuple[0], price = tuple[1];
                for (int nxt : graph.getOrDefault(stop, new ArrayList<>())) {
                    int tmpPrice = price + edges[stop][nxt];
                    if (nxt == dst) {
                        if (tmpPrice < ans) {
                            ans = tmpPrice;
                        }
                    } else if (tmpPrice < minPrices[nxt]) {
                        q.add(new int[]{nxt, tmpPrice});
                        minPrices[nxt] = tmpPrice;
                    }
                }
            }
            k--;
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}
