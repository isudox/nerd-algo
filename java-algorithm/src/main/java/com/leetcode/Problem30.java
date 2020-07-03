package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
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
        List<Integer> result = new ArrayList<>();
        if (words.length == 0)
            return result;
        List<String> wordList = Arrays.asList(words);
        int len = words[0].length();
        int sLen = s.length();
        if (len > sLen)
            return result;
        int wordsLen = len * (words.length);
        int i = 0;
        while (i <= sLen - wordsLen) {
            String word = s.substring(i, i + len);
            if (wordList.contains(word)) {
                String substr = s.substring(i, i + wordsLen);
                if (isValid(substr, wordList, len))
                    result.add(i);
            }
            i++;
        }
        return result;
    }

    private boolean isValid(String str, List<String> wordList, int len) {
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < str.length() / len; i++) {
            String s = str.substring(i * len, (i + 1) * len);
            list.add(s);
        }
        for (String s : wordList) {
            if (list.contains(s)) {
                list.remove(s);
            } else {
                return false;
            }
        }
        return true;
    }
}
