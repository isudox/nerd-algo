package com.leetcode;


import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 791. Custom Sort String
 * https://leetcode.com/problems/custom-sort-string/
 */
public class Problem791 {
    public String customSortString(String order, String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            map.put(order.charAt(i), i);
        }
        Character[] cs = new Character[s.length()];
        for (int i = 0; i < s.length(); i++) {
            cs[i] = s.charAt(i);
        }
        Arrays.sort(cs, (a, b) -> map.getOrDefault(a, 1000) - map.getOrDefault(b, 1001));
        StringBuilder sb = new StringBuilder();
        for (char c : cs) {
            sb.append(c);
        }
        return sb.toString();
    }
}
