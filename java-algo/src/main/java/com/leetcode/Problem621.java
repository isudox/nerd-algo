package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 621. Task Scheduler
 * https://leetcode.com/problems/task-scheduler/
 */
public class Problem621 {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> freq = new HashMap<>();
        int maxExec = 0;
        for (char ch : tasks) {
            int exec = freq.getOrDefault(ch, 0) + 1;
            freq.put(ch, exec);
            maxExec = Math.max(maxExec, exec);
        }
        int maxCount = 0;
        for (int value : freq.values()) {
            if (value == maxExec) {
                maxCount++;
            }
        }
        return Math.max((maxExec - 1) * (n + 1) + maxCount, tasks.length);
    }
}
