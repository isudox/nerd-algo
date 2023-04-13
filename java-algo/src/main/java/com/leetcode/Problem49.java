package com.leetcode;

import java.util.*;

/**
 * 49. Group Anagrams
 * https://leetcode.com/problems/group-anagrams/
 *
 * Given an array of strings, group anagrams together.
 *
 * Example:
 *
 * Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
 * Output:
 * [
 *   ["ate","eat","tea"],
 *   ["nat","tan"],
 *   ["bat"]
 * ]
 *
 * Note:
 *
 * All inputs will be in lowercase.
 * The order of your output does not matter.
 */
public class Problem49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();
        for (String str : strs) {
            String key = genKey(str);
            if (group.containsKey(key)) {
                group.get(key).add(str);
            } else {
                group.put(key, new ArrayList<>(Arrays.asList(str)));
            }

        }
        return new ArrayList<>(group.values());
    }

    private String genKey(String str) {
        StringBuilder key = new StringBuilder();
        int[] alph = new int[26];
        for (char c : str.toCharArray())
            alph[c - 'a'] += 1;
        for (int i = 0; i < 26; i++)
            if (alph[i] > 0)
                key.append((char) ('a' + i)).append(alph[i]);
        return key.toString();
    }

    public List<List<String>> groupAnagrams2(String[] strs) {
        Map<String, List<String>> store = new HashMap<>();
        for (String str : strs) {
            int[] count = new int[26];
            for (int i = 0; i < str.length(); i++) {
                count[str.charAt(i) - 'a']++;
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                if (count[i] > 0) {
                    sb.append((char) ('a' + i)).append(count[i]);
                }
            }
            String key = sb.toString();
            List<String> list = store.getOrDefault(key, new ArrayList<>());
            list.add(str);
            store.put(key, list);
        }
        return new ArrayList<>(store.values());
    }
}
