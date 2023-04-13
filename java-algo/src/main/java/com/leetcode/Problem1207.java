package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1207. Unique Number of Occurrences
 * https://leetcode.com/problems/unique-number-of-occurrences/
 */
public class Problem1207 {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> memo = new HashMap<>(2001);
        for (int num : arr) {
            memo.put(num, memo.getOrDefault(num, 0) + 1);
        }
        Map<Integer, Boolean> counter = new HashMap<>(memo.size());
        for (Integer value : memo.values()) {
            if (counter.containsKey(value)) return false;
            counter.put(value, true);
        }
        return true;
    }
}
