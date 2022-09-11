package com.leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * 1383. Maximum Performance of a Team
 * https://leetcode.com/problems/maximum-performance-of-a-team/
 */
public class Problem1383 {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        Integer[] indexes = new Integer[n];
        for (int i = 0; i < n; i++) indexes[i] = i;
        Arrays.sort(indexes, (i, j) -> efficiency[j] - efficiency[i]);
        PriorityQueue<Integer> pq = new PriorityQueue<>(k, (a, b) -> a - b);
        long ans = 0L;
        long sumSpeed= 0L;
        for (int i : indexes) {
            pq.offer(speed[i]);
            sumSpeed += speed[i];
            if (pq.size() > k) sumSpeed -= pq.poll();
            ans = Math.max(ans, sumSpeed * efficiency[i]);
        }
        return (int) (ans % (long) (1e9 + 7));
    }
}
