package com.leetcode;

import java.util.*;

/**
 * 815. Bus Routes
 * https://leetcode.com/problems/bus-routes/
 */
public class Problem815 {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;
        Deque<Integer> queue = new ArrayDeque<>();
        Map<Integer, Set<Integer>> stopBuses = new HashMap<>();
        Set<Integer> visitedBuses = new HashSet<>();
        for (int i = 0; i < routes.length; i++) {
            for (int stop : routes[i]) {
                if (stop == source)
                    queue.add(i);
                Set<Integer> buses = stopBuses.getOrDefault(stop, new HashSet<>());
                buses.add(i);
                stopBuses.put(stop, buses);
            }
        }
        int ans = 0;
        while (!queue.isEmpty()) {
            ans++;
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                int bus = queue.poll();
                for (int stop : routes[bus]) {
                    if (stop == target) return ans;
                    for (int nextBus : stopBuses.get(stop)) {
                        if (!visitedBuses.contains(nextBus)) {
                            queue.offer(nextBus);
                            visitedBuses.add(nextBus);
                        }
                    }
                }
            }
        }
        return -1;
    }
}
