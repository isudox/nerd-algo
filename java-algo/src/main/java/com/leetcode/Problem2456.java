package com.leetcode;

import java.util.*;

public class Problem2456 {
    public int[] secondGreaterElement(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        Deque<Integer> q = new ArrayDeque<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        for (int i = 0; i < n; i++) {
            while (!pq.isEmpty() && pq.peek()[0] < nums[i]) {
                ans[pq.poll()[1]] = nums[i];
            }
            while (!q.isEmpty() && nums[q.peek()] < nums[i]) {
                pq.offer(new int[]{nums[q.peek()], q.peek()});
                q.pop();
            }
            q.push(i);
        }
        return ans;
    }
}
