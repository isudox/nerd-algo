package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 159. Longest Substring with At Most Two Distinct Characters
 * https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
 */
public class Problem159 {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        char[] chars = s.toCharArray();
        char first = chars[0], second = chars[0];
        Map<Character, Integer> mark = new HashMap<>();
        int i = 0;
        int ans = 0;
        while (i < s.length()) {
            if (mark.containsKey(chars[i])) {
                i++;
            } else if (mark.size() < 2) {
                mark.put(chars[i], i);
                second = chars[i];
                i++;
            } else {
                ans = Math.max(ans, i - mark.get(first));
                mark.remove(first);
                first = second;
                i = mark.get(first);
            }
        }
        return Math.max(ans, s.length() - mark.get(first));
    }
}
