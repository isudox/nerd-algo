package com.leetcode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * 1834. Single-Threaded CPU
 * https://leetcode.com/problems/single-threaded-cpu/
 */
public class Problem1834 {
    public int[] getOrder(int[][] tasks) {
        int n = tasks.length;
        int[][] itasks = new int[n][3];
        for (int i = 0; i < n; i++) {
            itasks[i] = new int[]{tasks[i][0], tasks[i][1], i};
        }
        Arrays.sort(itasks, Comparator.comparingInt(a -> a[0]));
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[1] != b[1]) {
                return a[1] - b[1];
            }
            return a[2] - b[2];
        });
        int[] ans = new int[n];
        int time = 1, x = 0, i = 0;
        while (i < n) {
            while (x < n && itasks[x][0] <= time) {
                pq.add(itasks[x++]);
            }
            if (pq.isEmpty()) {
                time = itasks[x][0];
            } else {
                int[] cur = pq.poll();
                ans[i++] = cur[2];
                time += cur[1];
            }
        }
        return ans;
    }
}
