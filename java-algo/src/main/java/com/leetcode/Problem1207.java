package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

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
        Set<Integer> counter = new HashSet<>();
        for (Integer cnt : memo.values()) {
            if (counter.contains(cnt)) return false;
            counter.add(cnt);
        }
        return true;
    }
}
