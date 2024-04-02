package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 205. Isomorphic Strings
 * https://leetcode.com/problems/isomorphic-strings
 */
public class Problem205 {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Character> st = new HashMap<>(), ts = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i), b = t.charAt(i);
            if (st.containsKey(a) && st.get(a) != b) {
                return false;
            }
            if (ts.containsKey(b) && ts.get(b) != a) {
                return false;
            }
            st.put(a, b);
            ts.put(b, a);
        }
        return true;
    }
}
