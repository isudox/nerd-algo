package com.leetcode;

import java.util.*;

/**
 * 347. Top K Frequent Elements
 * https://leetcode.com/problems/top-k-frequent-elements/
 */
public class Problem347 {
    public int[] topKFrequent(int[] nums, int k) {
        PriorityQueue<Tuple> pq = new PriorityQueue<>(k, (o1, o2) -> o1.cnt - o2.cnt);
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            int num = entry.getKey();
            int cnt = entry.getValue();
            Tuple t = new Tuple(num, cnt);
            if (pq.size() < k) {
                pq.add(t);
            } else if (cnt > pq.peek().cnt) {
                pq.poll();
                pq.add(t);
            }
        }
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = pq.poll().num;
        }
        return ans;
    }

    private static class Tuple {
        private final int num;
        private final int cnt;

        public Tuple(int num, int cnt) {
            this.num = num;
            this.cnt = cnt;
        }
    }

}
