package com.leetcode;

/**
 * 1184. Distance Between Bus Stops
 * https://leetcode.com/problems/distance-between-bus-stops/
 */
public class Problem1184 {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        if (start == destination) return 0;
        if (start > destination) return distanceBetweenBusStops(distance, destination, start);
        int total = 0, cur = 0;
        for (int i = 0; i < distance.length; i++) {
            total += distance[i];
            if (start <= i && i < destination)
                cur += distance[i];
        }
        return Math.min(cur, total - cur);
    }
}
