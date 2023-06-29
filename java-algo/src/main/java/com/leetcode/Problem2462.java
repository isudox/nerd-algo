package com.leetcode;

import java.util.PriorityQueue;

/**
 * 2462. Total Cost to Hire K Workers
 * https://leetcode.com/problems/total-cost-to-hire-k-workers/
 */
class Problem2462 {
    public long totalCost(int[] costs, int k, int candidates) {
        int n = costs.length;
        int left = -1, right = -1;
        PriorityQueue<Integer> lq = new PriorityQueue<>((a, b) -> {
            if (costs[a] == costs[b]) {
                return a - b;
            }
            return costs[a] - costs[b];
        });
        PriorityQueue<Integer> rq = new PriorityQueue<>((a, b) -> {
            if (costs[a] == costs[b]) {
                return a - b;
            }
            return costs[a] - costs[b];
        });
        for (int i = 0; i < candidates; i++) {
            lq.add(i);
            left = i;
        }
        for (int i = 0; i < Math.min(candidates, n - candidates); i++) {
            rq.add(n - i - 1);
            right = n - i - 1;
        }
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int x = -1, y = -1;
            if (!lq.isEmpty()) {
                x = lq.peek();
            }
            if (!rq.isEmpty()) {
                y = rq.peek();
            }
            if (y == -1 || (x > -1 && costs[x] <= costs[y])) { // poll left queue
                ans += costs[x];
                lq.poll();
                if (lq.size() < candidates && right > left + 1) {
                    lq.add(++left);
                }
            } else { // poll right queue
                ans += costs[y];
                rq.poll();
                if (rq.size() < candidates && right > left + 1) {
                    rq.add(--right);
                }
            }
        }
        return ans;
    }
}
