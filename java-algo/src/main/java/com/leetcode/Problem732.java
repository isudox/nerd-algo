package com.leetcode;

import java.util.Map;
import java.util.TreeMap;

/**
 * 732. My Calendar III
 * https://leetcode.com/problems/my-calendar-iii
 */
public class Problem732 {
    private final TreeMap<Integer, Integer> map = new TreeMap<>();

    public Problem732() {
    }

    public int book(int start, int end) {
        map.put(start, map.getOrDefault(start, 0) + 1);
        map.put(end, map.getOrDefault(end, 0) - 1);
        int ret = 0, cnt = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            cnt += entry.getValue();
            if (cnt > ret) {
                ret = cnt;
            }
        }
        return ret;
    }
}
