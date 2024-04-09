package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 2073. Time Needed to Buy Tickets
 * https://leetcode.com/problems/time-needed-to-buy-tickets/
 */
public class Problem2073 {
    public int timeRequiredToBuy(int[] tickets, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < tickets.length; i++) {
            q.offerLast(i);
        }
        int time = 0;
        while (!q.isEmpty()) {
            time++;
            int i = q.pollFirst();
            if (i == k && tickets[i] == 1) {
                break;
            }
            tickets[i]--;
            if (tickets[i] > 0) {
                q.offerLast(i);
            }
        }
        return time;
    }
}
