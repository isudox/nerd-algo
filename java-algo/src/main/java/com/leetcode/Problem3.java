package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 */
public class Problem3 {
    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        int sLen = s.length();
        if (sLen == 0) {
            return 0;
        }
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < sLen; i++) {
            int curLen = 0;
            for (int j = i; j < sLen; j++) {
                char key = s.charAt(j);
                if (map.get(key) != null) {
                    map.clear();
                    break;
                }
                map.put(key, 1);
                curLen += 1;
                maxLen = Math.max(curLen, maxLen);
            }
        }
        return maxLen;
    }

}
