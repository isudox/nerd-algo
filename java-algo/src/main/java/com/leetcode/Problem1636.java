package com.leetcode;

import java.util.*;

/**
 * 1636. Sort Array by Increasing Frequency
 * https://leetcode.com/problems/sort-array-by-increasing-frequency/
 */
public class Problem1636 {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }
        list.sort((a, b) -> {
            if (counter.get(a).equals(counter.get(b)))
                return b - a;
            return counter.get(a) - counter.get(b);
        });
        return list.stream().mapToInt(i -> i).toArray();
    }
}
