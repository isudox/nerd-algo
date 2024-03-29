package com.leetcode;

import java.util.*;

/**
 * 451. Sort Characters By Frequency
 * https://leetcode.com/problems/sort-characters-by-frequency/
 */
public class Problem451 {
    public String frequencySort(String s) {
        TreeMap<Integer, List<Character>> map = new TreeMap<>(Collections.reverseOrder());
        Map<Character, Integer> count = new HashMap<>();
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : count.entrySet()) {
            List<Character> chars = map.getOrDefault(entry.getValue(), new ArrayList<>());
            chars.add(entry.getKey());
            map.put(entry.getValue(), chars);
        }
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<Integer, List<Character>> entry : map.entrySet()) {
            int cnt = entry.getKey();
            List<Character> chars = entry.getValue();
            for (char c : chars) {
                sb.append(String.valueOf(c).repeat(Math.max(0, cnt)));
            }
        }
        return sb.toString();
    }
}
