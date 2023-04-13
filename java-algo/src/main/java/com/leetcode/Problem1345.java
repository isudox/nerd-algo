package com.leetcode;

import java.util.*;

/**
 * 1345. Jump Game IV
 * https://leetcode.com/problems/jump-game-iv/
 */
public class Problem1345 {
    public int minJumps(int[] arr) {
        int n = arr.length;
        if (n == 1) return 0;
        Map<Integer, List<Integer>> store = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (!store.containsKey(arr[i])) {
                store.put(arr[i], new ArrayList<>());
            }
            store.get(arr[i]).add(i);
        }
        Queue<Integer> deque = new LinkedList<>();
        deque.add(0);
        int ans = 0;
        boolean[] visited = new boolean[n];
        while (deque.size() > 0) {
            Queue<Integer> nextQ = new LinkedList<>();
            for (int pos : deque) {
                if (pos == n - 1) {
                    return ans;
                }
                for (int nextPos : store.get(arr[pos])) {
                    if (!visited[nextPos]) {
                        visited[nextPos] = true;
                        nextQ.add(nextPos);
                    }
                }
                for (int nextPos : new int[]{pos - 1, pos + 1}) {
                    if (0 <= nextPos && nextPos < n && !visited[nextPos]) {
                        visited[nextPos] = true;
                        nextQ.add(nextPos);
                    }
                }
                store.get(arr[pos]).clear();
            }
            deque = nextQ;
            ans++;
        }
        return ans;
    }
}
