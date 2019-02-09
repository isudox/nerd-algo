package com.leetcode.solution;

import java.util.HashMap;
import java.util.Map;

/**
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * <p>
 * Given a string, find the length of the longest substring without repeating
 * characters.
 * <p>
 * Example 1:
 * <pre>
 *     Input: "abcabcbb"
 *     Output: 3
 *     Explanation: The answer is "abc", with the length of 3.
 * </pre>
 * <p>
 * Example 2:
 * <pre>
 *     Input: "bbbbb"
 *     Output: 1
 *     Explanation: The answer is "b", with the length of 1.
 * </pre>
 * <p>
 * Example 3:
 * <pre>
 *     Input: "pwwkew"
 *     Output: 3
 *     Explanation: The answer is "wke", with the length of 3.
 *                  Note that the answer must be a substring,
 *                  "pwke" is a subsequence and not a substring.
 * </pre>
 */
public class LongestSubstringWithoutRepeatingCharacters {

    public int lengthOfLongestSubstring(String s) {
        int maxLen = 0;
        int sLen = s.length();

        if (sLen == 0) {
            return 0;
        }

        for (int i = 0; i < sLen; i++) {
            int curLen = 0;
            Map<String, Integer> map = new HashMap<>();
            for (int j = i; j < sLen; j++) {
                String key = String.valueOf(s.charAt(j));
                if (map.get(key) == null) {
                    map.put(key, 1);
                    curLen += 1;
                    maxLen = curLen > maxLen ? curLen : maxLen;
                } else {
                    curLen = 0;
                    break;
                }
            }
        }

        return maxLen;
    }

}
