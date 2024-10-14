package com.leetcode;

import java.util.Collections;
import java.util.PriorityQueue;

/**
 * 2530. Maximal Score After Applying K Operations
 * https://leetcode.com/problems/maximal-score-after-applying-k-operations/
 */
public class Problem2530 {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int num : nums) {
            pq.add(num);
        }
        long ans = 0;
        for (int i = 0; i < k; i++) {
            int num = pq.poll();
            ans += num;
            pq.add((int) Math.ceil((double) num / 3));
        }
        return ans;
    }
}
