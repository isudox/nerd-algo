package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 953. Verifying an Alien Dictionary
 * https://leetcode.com/problems/verifying-an-alien-dictionary/
 */
public class Problem953 {
    private Map<Character, Integer> orders = new HashMap<>();

    public boolean isAlienSorted(String[] words, String order) {
        for (int i = 0; i < order.length(); i++) {
            this.orders.put(order.charAt(i), i);
        }
        for (int i = 0; i < words.length - 1; i++) {
            String a = words[i], b = words[i + 1];
            if (!compare(words[i], words[i + 1])) {
                return false;
            }
        }
        return true;
    }

    private boolean compare(String a, String b) {
        int i = 0, n = Math.min(a.length(), b.length());
        while (i < n) {
            if (orders.get(a.charAt(i)) < orders.get(b.charAt(i))) {
                return true;
            } else if (orders.get(a.charAt(i)) > orders.get(b.charAt(i))) {
                return false;
            } else {
                i++;
            }
        }
        return a.length() <= b.length();
    }
}
