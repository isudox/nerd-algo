package com.leetcode;

import java.util.*;


/**
 * 30. Substring with Concatenation of All Words
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/
 *
 * You are given a string, s, and a list of words, words,
 * that are all of the same length.
 * Find all starting indices of substring(s) in s that is a concatenation of
 * each word in words exactly once and without any intervening characters.
 *
 *
 *
 * Example 1:
 *
 * Input:
 *   s = "barfoothefoobarman",
 *   words = ["foo","bar"]
 * Output: [0,9]
 * Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
 * The output order does not matter, returning [9,0] is fine too.
 *
 * Example 2:
 *
 * Input:
 *   s = "wordgoodgoodgoodbestword",
 *   words = ["word","good","best","word"]
 * Output: []
 */
public class Problem30 {
    public List<Integer> findSubstring(String s, String[] words) {
        if (words.length == 0) {
            return new ArrayList<>();
        }
        int len = words[0].length();
        int sLen = s.length();
        if (len > sLen) {
            return new ArrayList<>();
        }
        Map<String, Integer> dict = new HashMap<>();
        for (String word : words) {
            dict.put(word, dict.getOrDefault(word, 0) + 1);
        }
        int wordsLen = len * (words.length);
        List<Integer> result = new ArrayList<>();
        int i = 0;
        while (i <= sLen - wordsLen) {
            String substr = s.substring(i, i + wordsLen);
            if (isValid(substr, dict, len)) {
                result.add(i);
            }
            i++;
        }
        return result;
    }

    private boolean isValid(String str, Map<String, Integer> dict, int len) {
        List<String> list = new ArrayList<String>();
        Map<String, Integer> counter = new HashMap<>();
        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            counter.put(entry.getKey(), entry.getValue());
        }
        for (int i = 0; i < str.length(); i += len) {
            String s = str.substring(i, i + len);
            if (counter.getOrDefault(s, 0) == 0) {
                return false;
            }
            counter.put(s, counter.get(s) - 1);
        }
        return true;
    }
}
