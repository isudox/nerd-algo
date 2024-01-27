package com.leetcode;

import java.util.PriorityQueue;

/**
 * https://leetcode.com/problems/take-gifts-from-the-richest-pile
 */
public class Problem2558 {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : gifts) {
            pq.offer(-num);
        }
        while (k > 0) {
            int max = -pq.poll();
            int rem = (int) Math.floor(Math.sqrt(max));
            pq.offer(-rem);
            k--;
        }
        long ans = 0;
        while (!pq.isEmpty()) {
            ans -= pq.poll();
        }
        return ans;
    }
}
