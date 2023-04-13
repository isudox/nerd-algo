package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 438. Find All Anagrams in a String
 * https://leetcode.com/problems/find-all-anagrams-in-a-string/
 */
public class Problem438 {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        int m = s.length(), n = p.length();
        if (m < n) {
            return ans;
        }
        Map<Character, Integer> pattern = new HashMap<>();
        for (char c : p.toCharArray()) {
            pattern.put(c, pattern.getOrDefault(c, 0) + 1);
        }
        char[] chars = s.toCharArray();
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < n; i++) {
            counter.put(chars[i], counter.getOrDefault(chars[i], 0) + 1);
        }
        int i = 0, j = n - 1;
        while (j < m) {
            if (compare(pattern, counter)) {
                ans.add(i);
            }
            if (j == m - 1) {
                break;
            }
            counter.put(chars[i], counter.get(chars[i]) - 1);
            if (counter.get(chars[i]) == 0) {
                counter.remove(chars[i]);
            }
            counter.put(chars[j + 1], counter.getOrDefault(chars[j + 1], 0) + 1);
            i++;
            j++;
        }
        return ans;
    }

    private boolean compare(Map<Character, Integer> m1, Map<Character, Integer> m2) {
        for (Map.Entry<Character, Integer> entry : m1.entrySet()) {
            Character ch = entry.getKey();
            int cnt = entry.getValue();
            if (!m2.containsKey(ch)) {
                return false;
            }
            if (m2.get(ch) != cnt) {
                return false;
            }
        }
        return true;
    }
}
