package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1657. Determine if Two Strings Are Close
 * https://leetcode.com/problems/determine-if-two-strings-are-close/
 */
public class Problem1657 {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        int[] count1 = new int[26], count2 = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            count1[word1.charAt(i) - 'a']++;
            count2[word2.charAt(i) - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            if (count1[i] == 0 && count2[i] != 0 || count1[i] != 0 && count2[i] == 0) {
                return false;
            }
        }
        Map<Integer, Integer> revCount = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            revCount.put(count1[i], revCount.getOrDefault(count1[i], 0) + 1);
            revCount.put(count2[i], revCount.getOrDefault(count2[i], 0) - 1);
        }
        for (Map.Entry<Integer, Integer> entry : revCount.entrySet()) {
            if (entry.getValue() != 0) {
                return false;
            }
        }
        return true;
    }
}
