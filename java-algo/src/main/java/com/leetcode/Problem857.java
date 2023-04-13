package com.leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * 857. Minimum Cost to Hire K Workers
 * https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
 */
public class Problem857 {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int[][] store = new int[quality.length][2];
        for (int i = 0; i < quality.length; i++) {
            store[i] = new int[]{quality[i], wage[i]};
        }
        Arrays.sort(store, (a, b) -> {
            int diff = a[1] * b[0] - b[1] * a[0];
            return diff == 0 ? a[1] - b[1] : diff;
        });
        double ans = 1e9;
        int total = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < k - 1; i++) {
            total += store[i][0];
            pq.offer(store[i][0]);
        }
        for (int i = k - 1; i < quality.length; i++) {
            total += store[i][0];
            pq.offer(store[i][0]);
            double cost = ((double) store[i][1] / store[i][0]) * total;
            ans = Math.min(ans, cost);
            total -= pq.poll();
        }
        return ans;
    }
}
