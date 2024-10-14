package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * 2406. Divide Intervals Into Minimum Number of Groups
 * https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
 */
public class Problem2406 {
    public int minGroups(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int[] interval : intervals) {
            if (!q.isEmpty() && q.peek() < interval[0]) {
                q.poll();
            }
            q.offer(interval[1]);
        }
        return q.size();
    }
}
