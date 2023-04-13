package com.leetcode;

import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * 264. Ugly Number II
 * https://leetcode.com/problems/ugly-number-ii/
 *
 * Given an integer n, return the n^th ugly number.
 *
 * Ugly number is a positive number whose prime factors only include 2, 3,
 * and/or 5.
 *
 * Example 1:
 *
 * Input: n = 10
 * Output: 12
 * Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
 * ugly numbers.
 *
 * Example 2:
 *
 * Input: n = 1
 * Output: 1
 * Explanation: 1 is typically treated as an ugly number.
 *
 * Constraints:
 * 1 <= n <= 1690
 */
public class Problem264 {
    public int nthUglyNumber(int n) {
        int[] dp = new int[n];
        dp[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for (int i = 1; i < n; i++) {
            int x2 = dp[p2] * 2, x3 = dp[p3] * 3, x5 = dp[p5] * 5;
            dp[i] = Math.min(Math.min(x2, x3), x5);
            if (dp[i] == x2)
                p2++;
            if (dp[i] == x3)
                p3++;
            if (dp[i] == x5)
                p5++;
        }
        return dp[n - 1];
    }
    public int nthUglyNumber2(int n) {
        int[] factors = new int[]{2, 3, 5};
        PriorityQueue<Long> pq = new PriorityQueue<>();
        Set<Long> memo = new HashSet<>();
        pq.offer(1L);
        int cur = 1;
        for (int i = 0; i < n; i++) {
            long min = pq.poll();
            cur = (int) min;
            for (int factor : factors) {
                long next = (long) cur * factor;
                if (!memo.contains(next)) {
                    pq.offer(next);
                }
                memo.add(next);
            }
        }
        return cur;
    }
}
