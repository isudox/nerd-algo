package com.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Problem1696 {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n]; // dp[i] = result to nums[i]
        dp[0] = nums[0];
        Deque<Integer> q = new ArrayDeque<>();
        q.offerLast(0);
        for (int i = 1; i < n; i++) {
            while (q.peekFirst() < i - k) {
                q.pollFirst();
            }
            dp[i] = dp[q.peekFirst()] + nums[i];
            while (!q.isEmpty() && dp[q.peekLast()] <= dp[i]) {
                q.pollLast();
            }
            q.offerLast(i);
        }
        return dp[n - 1];
    }
}
