package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 2053. Kth Distinct String in an Array
 */
public class Problem2053 {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> map = new HashMap<>();
        for (String s : arr) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
        int index = 0;
        for (String s : arr) {
            if (map.get(s) == 1) {
                index++;
                if (index == k) {
                    return s;
                }
            }
        }
        return "";
    }
}
