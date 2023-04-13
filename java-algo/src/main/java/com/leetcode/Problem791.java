package com.leetcode;

import java.util.*;

/**
 * 791. Custom Sort String
 * https://leetcode.com/problems/custom-sort-string/
 */
public class Problem791 {
    public String customSortString2(String order, String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            map.put(order.charAt(i), i);
        }
        Character[] cs = new Character[s.length()];
        for (int i = 0; i < s.length(); i++) {
            cs[i] = s.charAt(i);
        }
        Arrays.sort(cs, (a, b) -> map.getOrDefault(a, 100) - map.getOrDefault(b, 101));
        StringBuilder sb = new StringBuilder();
        for (char c : cs) {
            sb.append(c);
        }
        return sb.toString();
    }
}
