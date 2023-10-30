package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 274. H-Index
 * https://leetcode.com/problems/h-index
 */
public class Problem274 {
    public int hIndex(int[] citations) {
        int max = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int c : citations) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
            max = Math.max(max, c);
        }
        int cnt = 0;
        for (int i = max; i >= 1; i--) {
            cnt += counter.getOrDefault(i, 0);
            if (cnt >= i) {
                return i;
            }
        }
        return 0;
    }
}
