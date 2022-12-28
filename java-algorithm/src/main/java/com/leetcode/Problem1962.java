package com.leetcode;

import java.util.PriorityQueue;

/**
 * 1962. Remove Stones to Minimize the Total
 * https://leetcode.com/problems/remove-stones-to-minimize-the-total/
 */
public class Problem1962 {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int pile : piles) {
            pq.add(-pile);
        }
        for (int i = 0; i < k; i++) {
            int num = -pq.poll();
            num -= num / 2;
            pq.add(-num);
        }
        int ans = 0;
        while (!pq.isEmpty()) {
            ans += -pq.poll();
        }
        return ans;
    }
}
