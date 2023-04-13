package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 76. Minimum Window Substring
 * https://leetcode.com/problems/minimum-window-substring/
 */
class Problem76 {
    Map<Character, Integer> ori = new HashMap<>();
    Map<Character, Integer> cnt = new HashMap<>();

    public String minWindow(String s, String t) {
        int tLen = t.length();
        for (int i = 0; i < tLen; i++) {
            char c = t.charAt(i);
            ori.put(c, ori.getOrDefault(c, 0) + 1);
        }
        int i = 0, j = -1;
        int len = Integer.MAX_VALUE, l = -1, r = -1;
        while (j < s.length()) {
            ++j;
            if (j < s.length() && ori.containsKey(s.charAt(j))) {
                cnt.put(s.charAt(j), cnt.getOrDefault(s.charAt(j), 0) + 1);
            }
            while (check() && i <= j) {
                if (j - i + 1 < len) {
                    len = j - i + 1;
                    l = i;
                    r = i + len;
                }
                if (ori.containsKey(s.charAt(i))) {
                    cnt.put(s.charAt(i), cnt.getOrDefault(s.charAt(i), 0) - 1);
                }
                ++i;
            }
        }
        return l == -1 ? "" : s.substring(l, r);
    }

    public boolean check() {
        for (Map.Entry<Character, Integer> entry: ori.entrySet()) {
            Character key = entry.getKey();
            Integer val = entry.getValue();
            if (cnt.getOrDefault(key, 0) < val) {
                return false;
            }
        }
        return true;
    }
}
