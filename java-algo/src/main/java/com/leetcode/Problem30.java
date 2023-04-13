package com.leetcode;

import java.util.*;


/**
 * 30. Substring with Concatenation of All Words
 * https://leetcode.com/problems/substring-with-concatenation-of-all-words/
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

    public List<Integer> findSubstring2(String s, String[] words) {
        int m = words.length, n = words[0].length(), k = s.length();
        int win = m * n;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i + win > k) break;
            Map<String, Integer> store = new HashMap<>();
            for (int j = 0; j < m; j++) {
                String word = s.substring(i + j * n, i + (j + 1) * n);
                store.put(word, store.getOrDefault(word, 0) + 1);
            }
            for (String word : words) {
                store.put(word, store.getOrDefault(word, 0) - 1);
                if (store.get(word) == 0) store.remove(word);
            }
            for (int start = i; start < k - win + 1; start += n) {
                if (start != i) {
                    String word = s.substring(start + win - n, start + win);
                    store.put(word, store.getOrDefault(word, 0) + 1);
                    if (store.get(word) == 0) store.remove(word);
                    word = s.substring(start - n, start);
                    store.put(word, store.getOrDefault(word, 0) - 1);
                    if (store.get(word) == 0) store.remove(word);
                }
                if (store.isEmpty()) ans.add(start);
            }
        }
        return ans;
    }
}
