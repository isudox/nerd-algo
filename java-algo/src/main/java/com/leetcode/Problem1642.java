package com.leetcode;

import java.util.PriorityQueue;

/**
 * 1642. Furthest Building You Can Reach
 * https://leetcode.com/problems/furthest-building-you-can-reach/
 */
public class Problem1642 {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        int n = heights.length;
        int total = 0;
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int i = 1; i < n; i++) {
            int h = heights[i] - heights[i - 1];
            if (h > 0) {
                q.offer(h);
                if (q.size() > ladders) {
                    total += q.poll();
                }
                if (total > bricks) {
                    return i - 1;
                }
            }
        }
        return n - 1;
    }
}
