package com.leetcode;

import java.util.PriorityQueue;

public class Problem2530 {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : nums) {
            pq.add(-num);
        }
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int num = -pq.poll();
            ans += num;
            pq.add(-(int) Math.ceil((double) num / 3));
        }
        return ans;
    }
}
