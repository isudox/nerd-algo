package com.leetcode;

import java.util.TreeMap;

/**
 * 2418. Sort the People
 * https://leetcode.com/problems/sort-the-people
 */
public class Problem2418 {
    public String[] sortPeople(String[] names, int[] heights) {
        TreeMap<Integer, String> map = new TreeMap<>();
        for (int i = 0; i < names.length; i++) {
            map.put(heights[i], names[i]);
        }
        String[] ans = new String[names.length];
        int i = 0;
        for (int h : map.descendingKeySet()) {
            ans[i++] = map.get(h);
        }
        return ans;
    }
}
