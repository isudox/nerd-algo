package com.leetcode;

import java.util.PriorityQueue;

/**
 * 1801. Number of Orders in the Backlog
 * https://leetcode.com/problems/number-of-orders-in-the-backlog/
 */
public class Problem1801 {
    public int getNumberOfBacklogOrders(int[][] orders) {
        PriorityQueue<int[]> buyQueue = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        PriorityQueue<int[]> sellQueue = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int[] order : orders) {
            if (order[2] == 0) {  // buy
                if (sellQueue.isEmpty() || sellQueue.peek()[0] > order[0]) {
                    buyQueue.offer(order);
                    continue;
                }
                while (!sellQueue.isEmpty() && sellQueue.peek()[0] <= order[0] && order[1] > 0) {
                    int[] sellOrder = sellQueue.poll();
                    int cnt = Math.min(sellOrder[1], order[1]);
                    order[1] -= cnt;
                    sellOrder[1] -= cnt;
                    if (sellOrder[1] > 0) {
                        sellQueue.offer(sellOrder);
                    }
                }
                if (order[1] > 0) {
                    buyQueue.offer(order);
                }
            } else {  // sell
                if (buyQueue.isEmpty() || buyQueue.peek()[0] < order[0]) {
                    sellQueue.offer(order);
                    continue;
                }
                while (!buyQueue.isEmpty() && buyQueue.peek()[0] >= order[0] && order[1] > 0) {
                    int[] buyOrder = buyQueue.poll();
                    int cnt = Math.min(buyOrder[1], order[1]);
                    order[1] -= cnt;
                    buyOrder[1] -= cnt;
                    if (buyOrder[1] > 0) {
                        buyQueue.offer(buyOrder);
                    }
                }
                if (order[1] > 0) {
                    sellQueue.offer(order);
                }
            }
        }
        int mod = (int) 1e9 + 7, ans = 0;
        while (!buyQueue.isEmpty()) {
            ans = (ans + buyQueue.poll()[1]) % mod;
        }
        while (!sellQueue.isEmpty()) {
            ans = (ans + sellQueue.poll()[1]) % mod;
        }
        return ans;
    }
}
