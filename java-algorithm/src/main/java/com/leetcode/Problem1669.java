package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Problem1669 {
    public int maxResult(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        q.offer(0);
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[q.peekFirst()];
            while (!q.isEmpty() && nums[q.peekLast()] <= nums[i]) {
                q.pollLast();
            }
            q.offerLast(i);
            if (i - q.peekFirst() >= k) {
                q.pollFirst();
            }
        }
        return nums[nums.length - 1];
    }
}
