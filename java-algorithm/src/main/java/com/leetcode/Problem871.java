package com.leetcode;

import java.util.PriorityQueue;

/**
 * 871. Minimum Number of Refueling Stops
 * https://leetcode.com/problems/minimum-number-of-refueling-stops/
 */
public class Problem871 {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> o2 - o1);
        int n = stations.length;
        int ans = 0, fuel = startFuel;
        for (int i = 0; i <= n; i++) {
            int next = i < n ? stations[i][0] : target;
            int curr = i == 0 ? 0 : stations[i - 1][0];
            fuel = fuel - (next - curr);
            while (fuel < 0 && !pq.isEmpty()) {
                fuel += pq.poll();
                ans++;
            }
            if (fuel < 0) {
                return -1;
            }
            if (i < n) {
                pq.offer(stations[i][1]);
            }
        }
        return ans;
    }
}
